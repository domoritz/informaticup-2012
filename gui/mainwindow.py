from PyQt4.QtCore import QString, Qt, SIGNAL, SLOT
from PyQt4.QtGui import *
from gen.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

	def __init__(self, parent = None):
		QMainWindow.__init__(self, parent)

		self.setUnifiedTitleAndToolBarOnMac(True)

		self.setupUi(self)

