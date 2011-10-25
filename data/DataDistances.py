class DataDistances:
	"""Data structure containing distances between stores."""
	
	# Instance of DataMatrix (symmetric square matrix)
	distances = None

	def getDistance(self, i1, i2):
		"""Returns the minimum distance between i1 and i2."""
		return self.distances.getValue(i1, i2)
