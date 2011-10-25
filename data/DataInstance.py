class DataInstance:
	"""Data structure containing a problem set (instance)."""
	
	# Instance of DataPrices
	prices = None
	
	# Instance of DataDistances
	distances = None
	
	# Instance of DataPrices, containing orininal values (as read from the input file)
	originalPrices = None
	
	# Instance of DataDistances, containing original values (as read from the input file)
	originalDistances = None
	
	# Mapping Store index -> Store name (GUI only)
	storeIndexToName = None
	
	# Mapping Item index -> Item name (GUI only)
	itemIndexToName = None
	
	def getStoreNameByIndex(self, index):
		"""Returns a store's name (GUI only)."""
		return self.storeIndexToName(index)
		
	def getItemNameByIndex(self, index):
		"""Returns an item's name (GUI only)."""
		return self.itemIndexToName(index)
		
	def getStoreIndexByName(self, name):
		"""Returns a store's index (GUI only)."""
		for i in range(0, len(self.storeIndexToName)):
			if name == self.storeIndexToName[i]:
				return i
		return None
		
	def getItemIndexByName(self, name):
		"""Returns an item's index (GUI only)."""
		for i in range(0, len(self.itemIndexToName)):
			if name == self.itemIndexToName[i]:
				return i
		return None
