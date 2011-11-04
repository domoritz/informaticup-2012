import copy

class DataInstance(object):
	"""Data structure containing a problem set (instance)."""
	
	def __init__(self, instance = None):
		# Instance of DataPrices
		self.prices = None
		
		# Instance of DataDistances
		self.distances = None
		
		# Instance of DataPrices, containing orininal values (as read from the input file)
		self.originalPrices = None
		
		# Instance of DataDistances, containing original values (as read from the input file)
		self.originalDistances = None
		
		# Mapping Store index -> Store name (GUI only)
		self.storeIndexToName = None
		
		# Mapping Item index -> Item name (GUI only)
		self.itemIndexToName = None

		if instance:
			for attr in instance.__dict__.keys():
				setattr(self, attr, copy.deepcopy(getattr(instance, attr)))
	
	def getNumberStores(self):
		"""returns the number of stores"""
		return len(self.distances)

	def calculateCost(self, solution):
		"""docstring for calculateCost"""
		return 1
	
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
