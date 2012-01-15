from data.dataDistances import DataDistances
from data.dataPrices import DataPrices
from data.dataInstance import DataInstance
import csv, copy
import logging

class DataParser:
	"""Parser for reading problem sets (instances)."""

	def __init__(self):
		self.logger = logging.getLogger('shoppingtour')
	
	def readDistancesFile(self, distancesFile, aDataInstance):
		"""Parses a distances file into a DataDistances data structure."""
		r = csv.reader(distancesFile, delimiter=',')
		result = DataDistances()
		result.data = []
		firstRow = True
		rowCounter = 0

		for rowCounter,row in enumerate(r):
			if not firstRow:
				result.data.append([self.getNumeric(num) for num in row[1:]])
				
				if aDataInstance != None:
					aDataInstance.storeIndexToName[rowCounter - 1] = row[0]
			else:
				firstRow = False
		return result

	def readPricesFile(self, pricesFile, aDataInstance):
		"""Parses a prices file into a DataPrices data structure."""
		r = csv.reader(pricesFile, delimiter=',')
		result = DataPrices()
		result.data = []
		result.itemQuantity = []
		rowCounter = 0
		
		for rowCounter,row in enumerate(r):
			if rowCounter > 1:
				if aDataInstance != None:
					aDataInstance.itemIndexToName[rowCounter - 2] = row[0]

				result.data.append([self.getNumeric(num) for num in row[2:]])
				result.itemQuantity.append(row[1])
		return result

	def readInstance(self, pricesFile, distancesFile):
		"""Parses a prices file and a distances file into a DataInstance data structure."""
		result = DataInstance()
		result.itemIndexToName = {}
		result.storeIndexToName = {}

		result.originalPrices = self.readPricesFile(pricesFile, result)
		result.prices = copy.deepcopy(result.originalPrices).prepare()
		result.originalDistances = self.readDistancesFile(distancesFile, result)
		result.distances = copy.deepcopy(result.originalDistances).prepare()

		return result
		
	def getNumeric(self, value):
		"""Casts a value to a float value and returns None if impossible."""
		try:
			number = float(value)
			return number
		except Exception:
			return None
