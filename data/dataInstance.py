# -*- coding: utf-8 -*-
import copy
import logging

class DataInstance(object):
	"""Data structure containing a problem set (instance)."""
	
	def __init__(self, instance = None):
		self.logger = logging.getLogger('shoppingtour')

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
				if attr != 'logger':
					setattr(self, attr, copy.deepcopy(getattr(instance, attr)))
	
	def getShoppingList(self, solution):
		"""get shopping list according to the list of visited nodes"""
		shoppingList = {}
		for store in solution[1:]:
			shoppingList[store] = []

		for item in range(self.prices.getNumOfProducts()):
			infos = [(self.prices.getPrice(store, item), store) for store in solution if self.prices.getPrice(store, item) and store is not 0]
			infos.sort(key=lambda x: x[0])
			store = infos[0][1]
			price = infos[0][0]
			originalPrice = self.originalPrices.getPrice(store,item)
			quantity = self.originalPrices.itemQuantity[item]

			shoppingList[store].append((item,quantity,originalPrice))
		
		return shoppingList

	def getNumberStores(self):
		"""returns the number of stores"""
		return len(self.distances)

	def getNumberProducts(self):
		"""return number of products"""
		return len(self.prices)

	def calculateExpenses(self, solution):
		"""costs for travelling"""

		if solution[0]:
			#solution not valid, first node has to be home 
			return None

		numStores = len(solution)
		a = [ self.distances.data[solution[x]][solution[x+1]] for x in range(numStores-1) ]
		costsForTraveling = sum(a) + self.distances.data[solution[0]][solution[-1]]
		return costsForTraveling

	def calculateSpendings(self, solution):
		"""costs for buying"""
		costsForBuying = 0
		for item in range(self.prices.getNumOfProducts()):
			prices = [self.prices.getPrice(store, item) for store in solution if self.prices.getPrice(store, item) and store is not 0]
			if prices:
				costsForBuying += min(prices)
			else:
				#solution not valid
				return None
		return costsForBuying

	def calculateCost(self, solution):
		"""docstring for calculateCost"""
		spendings = self.calculateSpendings(solution)
		expenses = self.calculateExpenses(solution)

		if not spendings:
			#solution not valid
			return None

		if not expenses:
			#solution not valid
			return None
		
		return expenses + spendings
	
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
