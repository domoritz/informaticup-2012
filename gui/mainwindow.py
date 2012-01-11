from PyQt4.QtCore import QString, Qt, SIGNAL, SLOT, QRectF, QPointF
from PyQt4.QtGui import *
from gen.ui_mainwindow import Ui_MainWindow
from gui.opendialog import OpenDialog
from gui.algorithmThread import AlgorithmThread
from gui.positionCities import PositionCities

from program.dataParser import DataParser

import logging


class MainWindow(QMainWindow, Ui_MainWindow):

	def __init__(self, parent = None):
		QMainWindow.__init__(self, parent)
		self.logger = logging.getLogger('shoppingtour')


		self.setUnifiedTitleAndToolBarOnMac(True)

		self.setupUi(self)
		self.connect(self.actionOpen, SIGNAL('triggered(bool)'), self.open)
		self.connect(self.actionRun, SIGNAL('triggered(bool)'), self.run)
		self.openDialog = None
		self.dataInstance = None
		self.positionCities = None

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
		self.connect(thread, SIGNAL('nextSolution(QList<int>)'), self.nextSolution)
		self.connect(thread, SIGNAL('lastSolution(QList<int>)'), self.lastSolution)
		thread.start()

	def nextSolution(self, solution):
		self.logger.debug('nextSolution({0})'.format(solution))
		self.drawCities(self.positionCities.positions, self.dataInstance, solution)

	def lastSolution(self, solution):
		self.logger.debug('lastSolution({0})'.format(solution))
		self.drawCities(self.positionCities.positions, self.dataInstance, solution)
		self.statusBar().showMessage(self.tr('calculation finished'))

	def drawCities(self, positions, dataInstance, solution=None):
		scene = QGraphicsScene()

		usedWay = QPen(Qt.red)
		existingWay = QPen(Qt.black)
		usedWays = []
		if solution is not None:
			old = solution[-1]
			for i in solution:
				usedWays.append((old, i))
				usedWays.append((i, old))
				old = i

		for cityIndex in range(0, len(positions)):
			scene.addEllipse(QRectF(positions[cityIndex][0], positions[cityIndex][1], 25, 25))
			cityDescription = scene.addText(str(cityIndex))
			cityDescription.setPos(positions[cityIndex][0], positions[cityIndex][1])
		
		for city1 in range(0, len(dataInstance.originalDistances)):
			for city2 in range(0, len(dataInstance.originalDistances)):
				if dataInstance.originalDistances.getDistance(city1, city2) != None:
					scene.addLine(positions[city1][0]+12, positions[city1][1]+12, positions[city2][0]+12, positions[city2][1]+12,
					usedWay if (city1,city2) in usedWays else existingWay )

		self.graphicsView.setScene(scene)
		self.graphicsView.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
		self.graphicsView.show()

