from PyQt4.QtCore import QString, Qt, SIGNAL, SLOT, QRectF, QPointF
from PyQt4.QtGui import *
from gen.ui_mainwindow import Ui_MainWindow
from gui.opendialog import OpenDialog

class MainWindow(QMainWindow, Ui_MainWindow):

	def __init__(self, parent = None):
		QMainWindow.__init__(self, parent)

		self.setUnifiedTitleAndToolBarOnMac(True)

		self.setupUi(self)
		self.connect(self.actionOpen, SIGNAL('triggered(bool)'), self.open)

	def open(self):
		d = OpenDialog(self)
		d.exec_()
		print(d.getFileNames())
		print(d.getAlgorithmName())
		print(d.getAlgorithmOptions())
		

	def drawCities(self, positions, dataInstance):
		scene = QGraphicsScene()

		for cityIndex in range(0, len(positions)):
			scene.addEllipse(QRectF(positions[cityIndex][0], positions[cityIndex][1], 25, 25))
			cityDescription = scene.addText(str(cityIndex))
			cityDescription.setPos(positions[cityIndex][0], positions[cityIndex][1])
		
		for city1 in range(0, len(dataInstance.originalDistances)):
			for city2 in range(0, len(dataInstance.originalDistances)):
				if dataInstance.originalDistances.getDistance(city1, city2) != None:
					scene.addLine(positions[city1][0]+12, positions[city1][1]+12, positions[city2][0]+12, positions[city2][1]+12)

		self.graphicsView.setScene(scene)
		self.graphicsView.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
		self.graphicsView.show()

