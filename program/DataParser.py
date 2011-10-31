from data.DataDistances import DataDistances
from data.DataPrices import DataPrices
from data.DataInstance import DataInstance
import csv

print("loaded dataparser")

class DataParser:
	
	def readDistancesFile(self, distancesFile):
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
		result = DataInstance()
		result.prices = self.readPricesFile(pricesFile).prepare()
		result.originalPrices = self.readPricesFile(pricesFile)
		result.distances = self.readDistancesFile(distancesFile).prepare()
		result.originalDistances = self.readDistancesFile(distancesFile)
		
	def parserTest(self):
		print(self.readPricesFile(open('sample_data/prices1.txt', 'rb')).data)
		
	def getNumeric(self, value):
		try:
			number = float(value)
			return number
		except Exception:
			return None
