class DataPrices:
	"""Data structure containing prices of items."""
	
	# Instance of DataMatrix
	# 1st dimension (rows): store
	# 2nd dimension (columns): item
	# If item is not available: None
	prices = None

	def getPrice(self, store, item):
		"""Returns the price of an item in a specific store."""
		return self.prices.getValue(store, item)

	def getCheapestStore(self, item):
		"""Returns the store which sells 'item' cheapest."""
		return self.argmin(self.prices.getColumn(item))

	def getCheapestItem(self, store):
		"""Returns a store's cheapest item."""
		return self.argmin(self.prices.getRow(store))

	def argmin(list):
		"""Returns the index with minimum value inside a list."""
		listmin = min(list)
		for i in range(0, len(list)):
			if list[i] == listmin:
				return i
