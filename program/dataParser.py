from data.dataDistances import DataDistances
from data.dataPrices import DataPrices
from data.dataInstance import DataInstance
import csv, copy
import logging

class DataParser:
	"""Parser for reading problem sets (instances)."""

	def __init__(self):
		self.logger = logging.getLogger('shoppingtour')
	
	def readDistancesFile(self, distancesFile):
		"""Parses a distances file into a DataDistances data structure."""
		r = csv.reader(distancesFile, delimiter=',')
		result = DataDistances()
		result.data = []
		firstRow = True

		for row in r:
			if not firstRow:
				result.data.append([self.getNumeric(num) for num in row[1:]])
			else:
				firstRow = False
		return result

	def readPricesFile(self, pricesFile):
		"""Parses a prices file into a DataPrices data structure."""
		r = csv.reader(pricesFile, delimiter=',')
		result = DataPrices()
		result.data = []
		result.itemQuantity = []
		rowCounter = 0
		
		for row in r:
			if rowCounter > 1:
				result.data.append([self.getNumeric(num) for num in row[2:]])
				result.itemQuantity.append(row[1])
			rowCounter = rowCounter + 1
		result.removeQuantities()
		return result
		
	def readInstance(self, pricesFile, distancesFile):
		"""Parses a prices file and a distances file into a DataInstance data structure."""
		result = DataInstance()
		result.originalPrices =self.readPricesFile(pricesFile)
		result.prices = copy.deepcopy(result.originalPrices).prepare()
		result.originalDistances = self.readDistancesFile(distancesFile)
		result.distances = copy.deepcopy(result.originalDistances).prepare()
		
		return result
		
	def parserTest(self):
		"""Method for testing and debugging the parser."""
		testInstance = self.readInstance(open('sample_data/prices1.txt', 'rb'), open('sample_data/distances1.txt', 'rb'))
		
		self.logger.debug("original distances:")
		self.logger.debug(testInstance.originalDistances.data)
		
		self.logger.debug("prepared distances:")
		self.logger.debug(testInstance.distances.data)
		
	def getNumeric(self, value):
		"""Casts a value to a float value and returns None if impossible."""
		try:
			number = float(value)
			return number
		except Exception:
			return None
