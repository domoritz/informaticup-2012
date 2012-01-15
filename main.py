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
from program.settings import settings
from pprint import pformat

debug = False

algorithms = {
	'genetic':Genetic, 
	'clingo':Clingo,
	'none':None
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
	parser.add_argument('-i','--input', nargs=2, type=argparse.FileType('rb'), default=None, metavar=('prices.csv', 'distances.csv'),
				   help="set input files (csv) - first argument is prices, second is distances")
	parser.add_argument('-a','--algorithm', choices=algorithms.keys(), default=None, dest='algorithm',
				   help="select algorithm for coumputation")
	parser.add_argument('-v','--option', action='append', dest='options', default=[],
				   help='set program/algorithm option (option=value), see --list-options for availible options')
	parser.add_argument('-l','--list-options', action='store_true',
				   help='list all known options')
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

	formatter = logging.Formatter("%(relativeCreated)s %(name)s %(levelname)s: %(message)s")
	stderrHandler = logging.StreamHandler(sys.stderr)
	stderrHandler.setFormatter(formatter)
	logger.addHandler(stderrHandler)

	if args.list_options:
		def printOptions(options, prefix=''):
			for key in options:
				if type(options[key]) is dict:
					printOptions(options[key], prefix+key+'.')
				else:
					print('{0:30} {1}'.format(prefix+key, options[key]))
		print('{0:30} {1}'.format('Option', 'Default value'))
		print('-'*30+' '+'-'*20)
		printOptions(settings)
		return

	for optionString in args.options:
		option, sep, value = optionString.partition('=')
		if sep == '' or value == '':
			parser.error('option value "{0}" is not valid (format option=value)'.format(optionString))
		optionLevels = option.split('.')
		currentSettings = settings
		while len(optionLevels) > 1:
			currentOption = optionLevels.pop(0)
			if currentOption not in currentSettings:
				logger.warn('set unknown option {0}'.format(option))
				currentSettings[currentOption] = {}
			currentSettings = currentSettings[currentOption]
		if value.isdigit():
			value = int(value)
		currentSettings[optionLevels.pop(0)] = value

	if args.debug:
		logger.debug("=== DEBUG MODE ===")
		logger.debug("command line arguments:")
		for k in vars(args):
			logger.debug('{0}: {1}'.format(k,vars(args)[k]))

	if args.input and args.nogui:
		parser = DataParser()
		dataInstance = parser.readInstance(args.input[0],args.input[1])
		
		if algorithms[args.algorithm]:
			algo = algorithms[args.algorithm](dataInstance)

			solution = None
			for i in algo.generate():
				solution = i
				logger.info("Current solution: "+pformat(i)+" "+str(dataInstance.calculateCost(solution)))
				#print dataInstance.calculateSpendings(solution)
				#print dataInstance.calculateExpenses(solution)

			if solution:
				# print best solution
				logger.info("\nBest solution:\n==============")
				expenses = dataInstance.calculateExpenses(solution)
				spendings = dataInstance.calculateSpendings(solution)
				shoppingList = dataInstance.getShoppingList(solution)
				logger.info("Best Shopping Tour:\n"+pformat(solution))
				logger.info("Best Shopping Tour with known edges:\n"+pformat(dataInstance.distances.getRealPath(solution)))
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
		
		#if args.input: 
		#	logger.debug("positioning cities for gui")
		#	positionCities = PositionCities(dataInstance.distances)
		#	positionCities.optimize()

		logger.debug("initializing and running gui")

		#initialize and show ui
		QtCore.QCoreApplication.setOrganizationName('Hasso-Plattner-Institut');
		QtCore.QCoreApplication.setOrganizationDomain('hpi.uni-potsdam.de');
		QtCore.QCoreApplication.setApplicationName('shoppingtour');

		app = QtGui.QApplication(sys.argv)
		window = MainWindow(args = args)
		#window.setWindowState(QtCore.Qt.WindowMaximized)
		window.show()
		return app.exec_()		

if __name__ == "__main__":
	sys.exit(executeApplication())

