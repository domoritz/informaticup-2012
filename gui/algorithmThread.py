from PyQt4.QtCore import QThread, Qt, SIGNAL, SLOT, QRectF, QPointF, QCoreApplication, QEventLoop
from PyQt4.QtGui import *
import time

from program.genetic import Genetic
from program.clingo import Clingo

import logging

algorithms = {
	'genetic':Genetic,
	'clingo':Clingo
}

class AlgorithmThread(QThread):

	def __init__(self, dataInstance, algorithm, options, parent = None):
		QThread.__init__(self, parent)
		self.dataInstance  = dataInstance
		self.algorithm = algorithm
		self.options = options
		self.parent = parent

		self.logger = logging.getLogger('shoppingtour')

	def __del__(self):

		self.exiting = True
		self.wait()

	def run(self):
		algo = algorithms[self.algorithm](self.dataInstance, self.options)

		solution = None

		for count,i in enumerate(algo.generate()):
			if not count%100:
				QCoreApplication.processEvents(QEventLoop.AllEvents,100)
				time.sleep(0.05)
			if solution != i:
				self.logger.debug("improvement")
				solution = i
				self.emit(SIGNAL('nextSolution(QVariantList)'), i)
				time.sleep(0.1)
				QCoreApplication.processEvents(QEventLoop.AllEvents,100)

		self.emit(SIGNAL('lastSolution(QVariantList)'), i)
