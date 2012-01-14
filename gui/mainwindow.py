from PyQt4.QtCore import QString, Qt, SIGNAL, SLOT, QRectF, QPointF, QStringList, QRectF
from PyQt4.QtGui import *
from gen.ui_mainwindow import Ui_MainWindow
from gui.opendialog import OpenDialog
from gui.algorithmThread import AlgorithmThread
from gui.positionCities import PositionCities
from gui.graphWidget import GraphWidget, Edge, Node
from gen.ui_helpdialog import Ui_HelpDialog
from helpers.qt import Settings as QSettings

from program.dataParser import DataParser

import logging

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent = None):
		QMainWindow.__init__(self, parent)
		self.logger = logging.getLogger('shoppingtour')


		self.setUnifiedTitleAndToolBarOnMac(True)

		self.setupUi(self)

		self.loadSettings()

		#self.graphicsView = QGraphicsView(self.splitter)

		self.openDialog = None
		self.helpDialog = None
		self.dataInstance = None
		self.positionCities = None

		self.connect(self.actionOpen, SIGNAL('triggered(bool)'), self.open)
		self.connect(self.actionRun, SIGNAL('triggered(bool)'), self.run)
		self.connect(self.actionCancel, SIGNAL('triggered(bool)'), self.cancel)
		self.connect(self.actionHelp, SIGNAL('triggered(bool)'), self.help)

		self.nodes = []
		self.edges = {}

		self.progressGroupBox.setVisible(False)

	def open(self):
		if self.openDialog is None:
			self.openDialog = OpenDialog(self)
			self.openDialog.setModal(True)
			self.openDialog.setWindowModality(Qt.WindowModal)
		ret = self.openDialog.exec_()
		
		if ret == QDialog.Accepted:
			distancesFile, pricesFile = self.openDialog.getFileNames()
			self.logger.debug('opened: distances={0}, prices={1}'.format(distancesFile, pricesFile))
			self.logger.debug('algorithm: {0}'.format(self.openDialog.getAlgorithmName()))
			self.logger.debug('	options: {0}'.format(self.openDialog.getAlgorithmOptions()))
			parser = DataParser()
			self.dataInstance = parser.readInstance(open(pricesFile), open(distancesFile))
			self.positionCities = PositionCities(self.dataInstance.distances)
			self.positionCities.optimize()
			self.drawCities(self.positionCities.positions, self.dataInstance)

	def closeEvent(self, event):
		self.logger.info("Closing App")
		if self.helpDialog:
			self.helpDialog.close()
		if self.openDialog:
			self.openDialog.close()

		settings = QSettings()
		settings.beginGroup('windowSettings')
		settings.setValue("geometry", self.saveGeometry())
		settings.setValue("windowState", self.saveState())
		settings.endGroup()

	def loadSettings(self):
		settings = QSettings()
		geometry = settings.value("windowSettings/geometry", None)
		if geometry:
			self.restoreGeometry(geometry)
		state = settings.value("windowSettings/windowState", None)
		if state:
			self.restoreState(state)

	def help(self):
		if self.helpDialog is None:
			self.helpDialog = QDialog()
			Ui_HelpDialog().setupUi(self.helpDialog)
		self.helpDialog.open()

	def run(self):
		if self.openDialog is None:
			self.open()
		algorithmName = self.openDialog.getAlgorithmName()
		self.logger.debug('run: algorithm={0}'.format(algorithmName))
		self.thread = AlgorithmThread(
			self.dataInstance,
			algorithmName,
			self.openDialog.getAlgorithmOptions(),
			self)
		self.actionRun.setEnabled(False)
		self.actionCancel.setEnabled(True)
		self.statusBar.showMessage(self.tr('Calculation running'))
		self.connect(self.thread, SIGNAL('nextSolution(QVariantList)'), self.nextSolution)
		self.connect(self.thread, SIGNAL('lastSolution(QVariantList)'), self.lastSolution)
		self.connect(self.thread, SIGNAL('finished()'), self.calculationFinished)
		self.progressGroupBox.setVisible(True)
		self.thread.start()


	def nextSolution(self, solution):
		self.logger.debug('nextSolution({0})'.format(solution))
		self.updateCities(self.dataInstance, solution)
		self.showShoppingList(solution)
		self.showStats(solution)

	def lastSolution(self, solution):
		self.logger.debug('lastSolution({0})'.format(solution))
		self.updateCities(self.dataInstance, solution)
		self.statusBar.showMessage(self.tr('Calculation finished'))
		self.showShoppingList(solution)
		self.showStats(solution)
		self.progressGroupBox.setVisible(False)
		self.actionRun.setEnabled(True)
		self.actionCancel.setEnabled(False)

	def cancel(self):
		self.actionRun.setEnabled(True)
		self.actionCancel.setEnabled(False)
		self.progressGroupBox.setVisible(False)
		self.thread.terminate()
		self.statusBar.showMessage(self.tr('Calculation canceled'))

	def calculationFinished(self):
		if self.actionRun.isEnabled() is True: # lastSolution called
			return
		self.actionRun.setEnabled(True)
		self.actionCancel.setEnabled(False)
		self.progressGroupBox.setVisible(False)
		self.statusBar.showMessage(self.tr('Calculation terminated unexpected'))

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
		scene = QGraphicsScene(self.graphicsView)

		usedWays = []
		
		if solution is not None:
		
			old = solution[-1]
			for i in solution:
				usedWays.append((old, i))
				old = i

		for edge in self.edges:
			self.edges[edge].setVisible(False)

		for i1,city1 in enumerate(self.nodes):
			for i2,city2 in enumerate(self.nodes):
				if i1 != i2:
					edge = self.edges[(i1,i2)]
					edge.setVisible(False)
					original = dataInstance.originalDistances.getDistance(i1,i2) != None
					active = (i1, i2) in usedWays
					if original:
						edge.setVisible(True)
					if active:
						edge.text = str(dataInstance.distances.getDistance(i1,i2))
						edge.setActive(True)
					if active and not original:
						edge.setTempActive(True)

		self.graphicsView.updateScene([self.graphicsView.sceneRect()])	

	def drawCities(self, positions, dataInstance, solution=None):
		"""
		usedWay = QPen(QBrush(Qt.red),3)
		existingWay = QPen(QBrush(Qt.black),2)
		"""

		scene = QGraphicsScene(self.graphicsView)
		
		self.nodes = []
		for cityIndex in range(len(dataInstance.originalDistances)):
			node = Node(self.graphicsView, dataInstance.storeIndexToName[cityIndex])
			self.nodes.append(node)
			scene.addItem(node)

		for i1,city1 in enumerate(self.nodes):
			for i2,city2 in enumerate(self.nodes):
				if i1 != i2:
					edge = Edge(city1,city2,0)
					self.edges[(i1,i2)] = edge
					scene.addItem(edge)

		for cityIndex in range(len(positions)):
			self.nodes[cityIndex].setPos(positions[cityIndex][0], positions[cityIndex][1])

		self.graphicsView.setScene(scene)
		self.updateCities(dataInstance,solution)

		self.graphicsView.fitInView(self.graphicsView.sceneRect(),1)
		self.graphicsView.scale(0.9,0.9)
