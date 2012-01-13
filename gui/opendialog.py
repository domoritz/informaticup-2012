from PyQt4.QtCore import QString, Qt, SIGNAL, SLOT, QRectF, QPointF
from PyQt4.QtGui import *
from gen.ui_opendialog import Ui_OpenDialog
from helpers.qt import Settings as QSettings
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
		self.readSettings()
		self.connect(self, SIGNAL('accepted()'), self.saveSettings)

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

	def saveSettings(self):
		settings = QSettings()
		settings.beginGroup('openSettings')
		settings.setValue('distancesFile', self.distancesFileEdit.text())
		settings.setValue('pricesFileEdit', self.pricesFileEdit.text())
		settings.setValue('algorithm', self.getAlgorithmName())
		settings.endGroup()
		for algorithm in ['genetic', 'clingo']:
			options = self.getAlgorithmOptions(algorithm)
			settings.beginGroup(algorithm)
			for key in options:
				settings.setValue(key, options[key])
			settings.endGroup()

	def readSettings(self):
		settings = QSettings()
		settings.beginGroup('openSettings')
		self.distancesFileEdit.setText(settings.value('distancesFile', None) or self.distancesFileEdit.text())
		self.pricesFileEdit.setText(settings.value('pricesFile', None) or self.pricesFileEdit.text())
		self.setAlgorithmName(settings.value('algorithm', self.getAlgorithmName()))
		settings.endGroup()
		for algorithm in ['genetic', 'clingo']:
			options = self.getAlgorithmOptions(algorithm)
			settings.beginGroup(algorithm)
			for key in options:
				options[key] = settings.value(key, options[key])
			settings.endGroup()
			self.setAlgorithmOptions(algorithm, options)

	def getFileNames(self):
		return (str(self.distancesFileEdit.text()), str(self.pricesFileEdit.text()))

	def getAlgorithmName(self):
		if self.geneticButton.isChecked() is True:
			return 'genetic'
		if self.clingoButton.isChecked() is True:
			return 'clingo'

	def setAlgorithmName(self, name):
		if name == 'genetic':
			self.geneticButton.setChecked(True)
		if name == 'clingo':
			self.clingoButton.setChecked(True)

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

	def setAlgorithmOptions(self, algorithm, options):
		if algorithm == 'genetic':
			self.popSizeEdit.setValue(int(options['popsize']))
			self.childrenGroupEdit.setValue(int(options['childrenGroup']))
			self.mutationEdit.setValue(int(options['mutation']))
			self.shorteningEdit.setValue(int(options['shortening']))
			self.maxGenerationsEdit.setValue(int(options['maxGenerations']))
			self.stopAfterEdit.setValue(int(options['stopAfter']))
			self.seedEdit.setValue(int(options['seed']))
		if algorithm == 'clingo':
			self.clingoExecutableEdit.setText(options['clingo'])
			self.clingoArgsEdit.setText(options['clingoArgs'])
