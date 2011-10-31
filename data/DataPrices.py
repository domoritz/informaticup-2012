from data.DataMatrix import DataMatrix

class DataPrices(DataMatrix):
	"""Data structure containing prices of items."""
	
	# Instance of DataMatrix
	# 1st dimension (rows): store
	# 2nd dimension (columns): item
	# If item is not available: None

	def getPrice(self, store, item):
		"""Returns the price of an item in a specific store."""
		return self.getValue(store, item)

	def getCheapestStore(self, item):
		"""Returns the store which sells 'item' cheapest."""
		return self.argmin(self.getColumn(item))

	def getCheapestItem(self, store):
		"""Returns a store's cheapest item."""
		return self.argmin(self.getRow(store))

	def argmin(list):
		"""Returns the index with minimum value inside a list."""
		listmin = min(list)
		for i in range(0, len(list)):
			if list[i] == listmin:
				return i
