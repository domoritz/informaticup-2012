# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from gen.mainwindow import Ui_MainWindow 

def executeApplication():
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	return app.exec_()

if __name__ == "__main__":
	sys.exit(executeApplication())