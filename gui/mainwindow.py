from PyQt4.QtCore import QString, Qt, SIGNAL, SLOT, QRectF, QPointF, QStringList, QRectF
from PyQt4.QtGui import *
from gen.ui_mainwindow import Ui_MainWindow
from gui.opendialog import OpenDialog
from gui.algorithmThread import AlgorithmThread
from gui.positionCities import PositionCities
from gui.graphWidget import GraphWidget, Edge, Node
from gui.progressDialog import ProgressDialog

from program.dataParser import DataParser

import logging

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent = None):
		QMainWindow.__init__(self, parent)
		self.logger = logging.getLogger('shoppingtour')


		self.setUnifiedTitleAndToolBarOnMac(True)

		self.setupUi(self)

		#self.graphicsView = QGraphicsView(self.splitter) 

		self.connect(self.actionOpen, SIGNAL('triggered(bool)'), self.open)
		self.connect(self.actionRun, SIGNAL('triggered(bool)'), self.run)
		self.openDialog = None
		self.dataInstance = None
		self.positionCities = None

		self.nodes = {}
		self.edges = []

		self.progressDialog = ProgressDialog(self)
		self.progressDialog.setModal(True)
		#self.progressDialog.exec_()

	def open(self):
		if self.openDialog is None:
			self.openDialog = OpenDialog(self)
		self.openDialog.exec_()
		distancesFile, pricesFile = self.openDialog.getFileNames()
		self.logger.debug('opened: distances={0}, prices={1}'.format(distancesFile, pricesFile))
		self.logger.debug('algorithm: {0}'.format(self.openDialog.getAlgorithmName()))
		self.logger.debug('	options: {0}'.format(self.openDialog.getAlgorithmOptions()))
		parser = DataParser()
		self.dataInstance = parser.readInstance(open(pricesFile), open(distancesFile))
		self.positionCities = PositionCities(self.dataInstance.distances)
		self.positionCities.optimize()
		self.drawCities(self.positionCities.positions, self.dataInstance)


	def run(self):
		if self.openDialog is None:
			self.open()
		algorithmName = self.openDialog.getAlgorithmName()
		self.logger.debug('run: algorithm={0}'.format(algorithmName))
		thread = AlgorithmThread(
			self.dataInstance,
			algorithmName,
			self.openDialog.getAlgorithmOptions(),
			self)
		self.statusBar().showMessage(self.tr('Calculation running'))
		self.connect(thread, SIGNAL('nextSolution(QVariantList)'), self.nextSolution)
		self.connect(thread, SIGNAL('lastSolution(QVariantList)'), self.lastSolution)
		thread.start()

		self.progressDialog.show()

	def nextSolution(self, solution):
		self.logger.debug('nextSolution({0})'.format(solution))
		self.updateCities(self.dataInstance, solution)
		self.showShoppingList(solution)
		self.showStats(solution)

	def lastSolution(self, solution):
		self.logger.debug('lastSolution({0})'.format(solution))
		self.updateCities(self.dataInstance, solution)
		self.statusBar().showMessage(self.tr('Calculation finished'))
		self.showShoppingList(solution)
		self.showStats(solution)

		self.progressDialog.hide()

	def showShoppingList(self, solution):
		self.shoppingTree.clear()
		shoppingList = self.dataInstance.getShoppingList(solution)
		for store in shoppingList:
			storeName = self.dataInstance.storeIndexToName[store]
			rootItem = QTreeWidgetItem(self.shoppingTree,QStringList([storeName,"","",""]))
			for item,quantity,originalPrice in shoppingList[store]:
				subitem = QTreeWidgetItem(rootItem,QStringList([storeName,self.dataInstance.itemIndexToName[item],str(quantity),str(originalPrice)]))

			rootItem.setExpanded(True)
			self.shoppingTree.addTopLevelItem(rootItem)
	
	def showStats(self, solution):
		expenses = self.dataInstance.calculateExpenses(solution)
		spendings = self.dataInstance.calculateSpendings(solution)
		self.expenses.setText(str(expenses))
		self.spendings.setText(str(spendings))
		self.total.setText(str(expenses+spendings))

	def updateCities(self, dataInstance, solution):
		usedWays = []
		if solution is not None:
			old = solution[-1]
			for i in solution:
				usedWays.append((old, i))
				usedWays.append((i, old))
				old = i

		for i1,city1 in enumerate(self.nodes):
			for i2,city2 in enumerate(self.nodes):
				if (i1, i2) in usedWays :
					self.edges[(i1,i2)].setActive()

	def drawCities(self, positions, dataInstance, solution=None):
		"""scene = QGraphicsScene()
		self.graphicsView.setScene(scene)

		usedWay = QPen(QBrush(Qt.red),3)
		existingWay = QPen(QBrush(Qt.black),2)

		usedWays = []
		if solution is not None:
			old = solution[-1]
			for i in solution:
				usedWays.append((old, i))
				usedWays.append((i, old))
				old = i

		for city1 in range(0, len(dataInstance.originalDistances)):
			for city2 in range(0, len(dataInstance.originalDistances)):
				if dataInstance.originalDistances.getDistance(city1, city2) != None:
					scene.addLine(positions[city1][0]+12, positions[city1][1]+12, positions[city2][0]+12, positions[city2][1]+12, usedWay if (city1,city2) in usedWays else existingWay )

		for cityIndex in range(0, len(positions)):
			scene.addEllipse(QRectF(positions[cityIndex][0], positions[cityIndex][1], 30, 30), QPen(), QBrush(QColor(255,255,255), Qt.SolidPattern))
			cityDescription = scene.addText(dataInstance.storeIndexToName[cityIndex], QFont())
			cityDescription.setPos(positions[cityIndex][0], positions[cityIndex][1])
		"""

		scene = QGraphicsScene(self.graphicsView)
		
		self.nodes = []
		for cityIndex in range(len(dataInstance.originalDistances)):
			node = Node(self.graphicsView, dataInstance.storeIndexToName[cityIndex])
			self.nodes.append(node)
			scene.addItem(node)

		for i1,city1 in enumerate(self.nodes):
			for i2,city2 in enumerate(self.nodes):
				if i1 > i2 and dataInstance.originalDistances.getDistance(i1,i2) != None:
					edge = Edge(city1,city2)
					self.edges[(i1,i2)] = edge
					scene.addItem(edge)

		for cityIndex in range(len(positions)):
			self.nodes[cityIndex].setPos(positions[cityIndex][0], positions[cityIndex][1])


		self.graphicsView.setScene(scene)

		self.graphicsView.fitInView(self.graphicsView.sceneRect(),1)
		self.graphicsView.scale(0.9,0.9)
