from data.DataMatrix import DataMatrix

class DataDistances(DataMatrix):
	"""Data structure containing distances between stores."""

	def __len__(self):
		return len(self.data)
		
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
		
		for i in range(0, len(self.data)):
			self.shortestDistances.append(list(self.data[i]))
			self.shortestPaths.append([None for i in range(0, len(self.data))])
			
		for k in range(0, len(self.data)):
			for i in range(0, len(self.data)):
				for j in range(0, len(self.data)):
					compositePathLength = addNumbersNone(self.shortestDistances[i][k], self.shortestDistances[k][j])
					
					if self.shortestDistances[i][j] < compositePathLength and self.shortestDistances[i][j] != None:
						self.shortestPaths[i][j] = j
					elif compositePathLength != None:
						self.shortestPaths[i][j] = k
						self.shortestDistances[i][j] = compositePathLength
						
		for i in range(0, len(self.data)):
			for j in range(0, len(self.data)):
				if self.data[i][j] == None:
					self.data[i][j] = self.shortestDistances[i][j]
					
		return self
