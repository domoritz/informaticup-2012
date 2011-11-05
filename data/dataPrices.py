from data.dataMatrix import DataMatrix

class DataPrices(DataMatrix):
	"""Data structure containing prices of items."""
	# Instance of DataMatrix
	# 1st dimension (rows): item
	# 2nd dimension (columns): store
	# If item is not available: None

	# This list usually contains only ones.
	itemQuantity = None
	
	def getPrice(self, store, item):
		"""Returns the price of an item in a specific store."""
		return self.getValue(item, store)

	def getCheapestStore(self, item):
		"""Returns the store which sells 'item' cheapest."""
		return self.argmin(self.getColumn(item))

	def getCheapestItem(self, store):
		"""Returns a store's cheapest item."""
		return self.argmin(self.getRow(store))

	def argmin(list):
		"""Returns the index with minimum value inside a list."""
		#TODO rewrite!!!!
		listmin = min(list)
		for i in range(0, len(list)):
			if list[i] == listmin:
				return i

	def removeQuantities(self):
		"""Sets all quantities to 1 and adds that information to item prices."""
		for i in range(0, len(self.itemQuantity)):
			for j in range(0, len(self.data[i])):
				if self.isNumeric(self.data[i][j]) and self.isNumeric(self.itemQuantity[i]):
					self.data[i][j] = self.data[i][j] * float(self.itemQuantity[i])
			self.itemQuantity[i] = 1
		return self
	
	def prepare(self):
		"""Prepares the data structure for the next steps (algorithms, ...) and makes optimizations."""
		self.removeQuantities()
		return self
		
	def isNumeric(self, value):
		"""Evaluates whether a value is numeric."""
		try:
			number = float(value)
			return True
		except Exception:
			return False
			
