from data.dataInstance import DataInstance

class Algorithm(DataInstance):
	""" Abstract class for algorithms """

	def solve(self, solution = None):
		"""returns the final solution for the algorithm"""
		finalSolution = None
		for element in self.generate(solution):
			finalSolution = element
		return finalSolution

	def generate(solution = None):
		"""creates a solution and yields it as a list 
		of numbers which stand for the shops
		i.e. [4,6,2,3,1,5]
		this means, solve is a generator
		"""
		pass
