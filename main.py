#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import argparse

from helpers.output import ShoppingTourLogger
from program.dataParser import DataParser
from program.algorithm import Algorithm
from program.genetic import Genetic
from program.clingo import Clingo
from pprint import pformat

debug = False

algorithms = {
	'genetic':Genetic, 
	'clingo':Clingo
}

def executeApplication():
	#do non UI stuff
	parser = argparse.ArgumentParser(prog='Shoppingtour', description='Calculates cheapest shopping tour.', epilog='Let us do the work.')
	parser.add_argument('-c','--commandline', action='store_true', dest='nogui',
				   help="don't use a graphical user interface")
	parser.add_argument('-d','--debug', action='store_true',
				   help="print debug information to stdout")
	parser.add_argument('-o','--output', nargs=1, type=argparse.FileType('w'),
				   default=sys.stdout, help='write results to FILE (default is stdout)')
	parser.add_argument('-i','--input', nargs=2, required=True, type=argparse.FileType('rb'), metavar=('prices.csv', 'distances.csv'),
				   help="set input files (csv) - first argument is prices, second is distances")
	parser.add_argument('-a','--algorithm', choices=algorithms.keys(), default='clingo', dest='algorithm',
				   help="select algorithm for coumputation")
	parser.add_argument('--version', action='version', version='%(prog)s 1.0')

	#parse arguments
	args = parser.parse_args()

	global debug
	debug = args.debug

	logging.setLoggerClass(ShoppingTourLogger)
	logger = logging.getLogger('shoppingtour')
	if args.debug:
		logger.setLevel(logging.DEBUG)
	else:
		logger.setLevel(logging.INFO)

	formatter = logging.Formatter("%(relativeCreated)s ms - %(name)s - %(levelname)s: %(message)s")
	stderrHandler = logging.StreamHandler(sys.stderr)
	stderrHandler.setFormatter(formatter)
	logger.addHandler(stderrHandler)

	if args.debug:
		logger.debug("=== DEBUG MODE ===")
		logger.debug("command line arguments:")
		for k in vars(args):
			logger.debug('{0}: {1}'.format(k,vars(args)[k]))

	if args.input:
		parser = DataParser()
		dataInstance = parser.readInstance(args.input[0],args.input[1])
		
		algo = algorithms[args.algorithm](dataInstance)

		for i in algo.generate():
			solution = i
			logger.info("Current solution: "+pformat(i))

		if i:
			# print best solution
			logger.warn("\nBest solution:\n==============")
			expenses = dataInstance.calculateExpenses(i)
			spendings = dataInstance.calculateSpendings(i)
			shoppingList = dataInstance.getShoppingList(i)
			logger.info("Best Shopping Tour:\n"+pformat(i))
			logger.info("Shopping List:\n"+pformat(shoppingList))
			logger.info("Total Costs: "+str(spendings+expenses))
			logger.info("Spendings: "+str(spendings))
			logger.info("Expenses: "+str(expenses))
		else:
			logger.warn("No solution found")

	if not args.nogui:
		from PyQt4 import QtCore, QtGui
		from gui.mainwindow import MainWindow 
		from gui.positionCities import PositionCities
		
		logger.debug("positioning cities for gui")
		positionCities = PositionCities(dataInstance.distances)
		positionCities.optimize()
		if debug: positionCities.debugPrint()

		logger.debug("initializing and running gui")
		#initialize and show ui
		app = QtGui.QApplication(sys.argv)
		window = MainWindow()
		window.drawCities(positionCities.positions, dataInstance)
		window.show()
		return app.exec_()		

if __name__ == "__main__":
	sys.exit(executeApplication())

