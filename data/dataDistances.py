from data.dataMatrix import DataMatrix

class DataDistances(DataMatrix):
	"""Data structure containing distances between stores."""
		
	def getDistance(self, i1, i2):
		"""Returns the minimum distance between i1 and i2."""
		return self.getValue(i1, i2)

	def prepare(self):
		"""Prepares the data structure for the next steps (algorithms, ...) and makes optimizations."""
		return self.generateFullGraph()
	
	def generateFullGraph(self):
		"""Floyd-Worshall alorithm used for finding the shortest paths"""
		self.shortestDistances = []
		self.shortestPaths = []
		addNumbersNone = lambda x, y: x + y if x != None and y != None else None
		
		# Creating data structure for floyd-warshall
		for i in range(0, len(self.data)):
			self.shortestDistances.append(list(self.data[i]))
			self.shortestPaths.append([None for i in range(0, len(self.data))])
		
		# For all pairs of cities set shortestPath[a][b] = b, i.e. b is reachable from a via b
		for i in range(0, len(self.data)):
			for j in range(0, len(self.data)):
				self.shortestPaths[i][j] = j
				
		# Try to find shorter routes via k ...
		for k in range(0, len(self.data)):
			# ... for all pairs of cities (i, j)
			for i in range(0, len(self.data)):
				for j in range(0, len(self.data)):
					# compositePathLength = distance from i to j via k
					# compositePathLength == None <=> no such path
					compositePathLength = addNumbersNone(self.shortestDistances[i][k], self.shortestDistances[k][j])
					
					if compositePathLength != None:
						if self.shortestDistances[i][j] == None:
							# There was no direct edge between (i,j) in the original graph, let's fill the gap
							self.shortestDistances[i][j] = compositePathLength
							self.shortestPaths[i][j] = k
						elif compositePathLength < self.shortestDistances[i][j]:
							# We found a shorter path from i to j
							self.shortestPaths[i][j] = k
							self.shortestDistances[i][j] = compositePathLength

		# Modify actual data structure such that it doesn't contain None anymore
		for i in range(0, len(self.data)):
			for j in range(0, len(self.data)):
				if self.data[i][j] == None:
					self.data[i][j] = self.shortestDistances[i][j]
					
		return self
		
	def getRealPath(self, solution):
		"""Retrieves an actual path from a given path without taking edges that don't exist in the original graph. The neccessary information was saved during Floyd-Warhshall."""
		# Start with the first city
		shortestPath = [solution[0]]

		# Traverse all cities in the correct order
		for city in range(0, len(solution) - 1):
			currentCity = solution[city]
			destinationCity = solution[city + 1]
			
			# Use shortestPaths to get the real path from currentCity to destinationCity
			while currentCity != destinationCity:
				nextCity = self.shortestPaths[currentCity][destinationCity]
				shortestPath.append(nextCity)
				currentCity = nextCity

		return shortestPath
