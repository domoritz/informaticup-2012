from PyQt4.QtCore import QString, Qt, SIGNAL, SLOT, QRectF, QPointF
from PyQt4.QtGui import *
from gen.ui_opendialog import Ui_OpenDialog
import os


class OpenDialog(QDialog, Ui_OpenDialog):

	def __init__(self, parent = None):
		QDialog.__init__(self, parent)

		self.setupUi(self)

		self.connect(self.distancesFileButton, SIGNAL('clicked()'), self.selectDistances)
		self.connect(self.pricesFileButton, SIGNAL('clicked()'), self.selectPrices)
		self.connect(self.geneticButton, SIGNAL('toggled(bool)'), self.geneticOptions.setEnabled)
		self.connect(self.clingoButton, SIGNAL('toggled(bool)'), self.clingoOptions.setEnabled)
		self.clingoButton.setChecked(True)

	def selectDistances(self):
		self.runOpenFileDialog(self.distancesFileEdit)

	def selectPrices(self):
		self.runOpenFileDialog(self.pricesFileEdit)

	def runOpenFileDialog(self, edit):
		last = edit.text()
		edit.setText(QFileDialog.getOpenFileName (self, 
			self.tr('Select file'), # caption
			os.path.abspath(str(last)), #caption
			))

	def selectCorrectOptionBlock(self):
		self

	def getFileNames(self):
		return (str(self.distancesFileEdit.text()), str(self.pricesFileEdit.text()))

	def getAlgorithmName(self):
		if self.geneticButton.isChecked() is True:
			return 'genetic'
		if self.clingoButton.isChecked() is True:
			return 'clingo'

	def getAlgorithmOptions(self, algorithm=None):
		if algorithm is None:
			algorithm = self.getAlgorithmName()
		if algorithm == 'genetic':
			return {
				'popsize': self.popSizeEdit.value(),
				'childrenGroup': self.childrenGroupEdit.value(),
				'mutation': self.mutationEdit.value(),
				'shortening': self.shorteningEdit.value(),
				'maxGenerations': self.maxGenerationsEdit.value(),
				'stopAfter': self.stopAfterEdit.value(),
				'seed': self.seedEdit.value()
			}
		if algorithm == 'clingo':
			return {
				'clingo': str(self.clingoExecutableEdit.text()),
				'clingoArgs': str(self.clingoArgsEdit.text())
			}
