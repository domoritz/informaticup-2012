#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import argparse

from helpers.output import ShoppingTourLogger
from program.dataParser import DataParser
from program.genetic import Genetic


debug = False

def executeApplication():
	#do non UI stuff
	parser = argparse.ArgumentParser(prog='Shoppingtour', description='Calculates cheapest shopping tour.', epilog='Let us do the work.')
	parser.add_argument('-c','--commandline', action='store_true', dest='nogui',
				   help="don't use a graphical user interface")
	parser.add_argument('-d','--debug', action='store_true',
				   help="print debug information to stdout")
	parser.add_argument('-o','--output', nargs=1, type=argparse.FileType('w'),
				   default=sys.stdout, help='write results to FILE (default is stdout)')
	parser.add_argument('-i','--input', nargs=2, type=argparse.FileType('rb'), metavar=('prices.csv', 'distances.csv'),
				   help="set input files (csv) - first argument is prices, second is distances")
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
		logger.setLevel(logging.WARN)
	formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
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

		algo = Genetic(dataInstance)
		for i in algo.generate():
			logger.info(i)
			solution = i
		logger.info("Best Solution:")
		logger.info(i)
		logger.info(dataInstance.calculateSpendings(i[0]))
		logger.info(dataInstance.calculateExpenses(i[0]))

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

