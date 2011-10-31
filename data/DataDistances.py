from data.DataMatrix import DataMatrix

class DataDistances(DataMatrix):
	"""Data structure containing distances between stores."""

	def getDistance(self, i1, i2):
		"""Returns the minimum distance between i1 and i2."""
		return self.getValue(i1, i2)

	def prepare(self):
		return self
		