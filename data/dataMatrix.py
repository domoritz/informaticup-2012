class DataMatrix:
	"""A 2-dimensional matrix."""

	def __init__(self):
		"""docstring for __init__"""
		# 2-dimensional list which contains the actual data
		# e.g. data = [ ['r', 'o', 'w', '1'], ['r', 'o', 'w', '2'] ]
		self.data = None

	def __len__(self):
		return len(self.data)

	def getColumn(self, index):
		"""Returns a value copy of a specific column in the matrix."""
		return [row[index] for row in self.data]

	def getRow(self, index):
		"""Returns a value copy of a specific row in the matrix."""
		return self.data[index][:]

	def getValue(self, i1, i2):
		"""Returns a specific value in the matrix. i1 is the row index and i2 is the column index."""
		return self.data[i1][i2]
