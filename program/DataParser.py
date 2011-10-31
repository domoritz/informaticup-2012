from data.DataDistances import DataDistances
from data.DataPrices import DataPrices
import csv

print("loaded dataparser")

class DataParser:
	
	def readDistancesFile(self, filename):
		r = csv.reader(open(filename, 'rb'), delimiter=',')
		result = DataDistances()
		result.data = []
		firstRow = True
		
		for row in r:
			if not firstRow:
				result.data.append([self.getNumeric(num) for num in row[1:]])
			else:
				firstRow = False
				
		return result

	def readPricesFile(self, filename):
		r = csv.reader(open(filename, 'rb'), delimiter=',')
		result = DataPrices()
		result.data = []
		# Work to do..
		
	def readInstance(self, pricesFile, distancesFile):
		pass
		
	def parserTest(self):
		print(self.readDistancesFile('sample_data/distances1.txt').data)
		
	def getNumeric(self, value):
		try:
			number = float(value)
			return number
		except ValueError:
			return None
