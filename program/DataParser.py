from data.DataDistances import DataDistances
from data.DataPrices import DataPrices
import csv

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
		# Work to do..
		
	def readInstance(self, pricesFile, distancesFile):
		pass
		
	def parserTest(self):
		print(self.readDistancesFile(open('sample_data/distances1.txt', 'rb')).data)
		
	def getNumeric(self, value):
		try:
			number = float(value)
			return number
		except ValueError:
			return None
