from PyQt4.QtCore import QString, Qt, SIGNAL, SLOT, QRectF, QPointF, QStringList, QRectF
from PyQt4.QtGui import *
from gen.ui_mainwindow import Ui_MainWindow
from gui.opendialog import OpenDialog
from gui.algorithmThread import AlgorithmThread
from gui.positionCities import PositionCities
from gui.graphWidget import GraphWidget

from program.dataParser import DataParser

import logging


class ProgressDialog(QDialog):
    def __init__(self, Parent=None):
        super(ProgressDialog, self).__init__()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel)
        label = QLabel("Calculating")
        progressbar = QProgressBar()
        progressbar.setMaximum(0)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(progressbar)
        layout.addWidget(buttonBox)
        self.setLayout(layout)
        self.setWindowTitle("Calculating")
