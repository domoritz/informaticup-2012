from PyQt4.QtCore import QThread, Qt, SIGNAL, SLOT, QRectF, QPointF
from PyQt4.QtGui import *

from program.genetic import Genetic
from program.clingo import Clingo

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

	def run(self):
		algo = algorithms[self.algorithm](self.dataInstance, self.options)

		for i in algo.generate():
			solution = i
			self.emit(SIGNAL('nextSolution(QList<int>)'), i)

		self.emit(SIGNAL('lastSolution(QList<int>)'), i)

