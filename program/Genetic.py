from data.DataInstance import DataInstance
from program.Algorithm import Algorithm
import random

class Genetic(Algorithm):
	""" Genetic algorithm """

	def __init__(self, data, options = None):
		super(Genetic, self).__init__(data)

		if options:
			self.options = options
		else:
			options = {
				"popsize":10,
				"childrenGroup": 2,
				"mutation": 3,
				"maxGenerations": 100,
				"seed": 1
			}
		self.population = []
		random.seed(options['seed'])

	def generate(solution = None):
		"""creates a solution and yields it as a list 
		of numbers which stand for the shops
		i.e. [4,6,2,3,1,5]
		this means, solve is a generator
		"""
		if False:
			yield None

	def brew(self):
		"""generate a population"""
		numberCities = 10
		self.population = [[random.randint(0,numberCities-y) for y in range(numberCities-1)] for x in range(options.popsize)]

	def evaluate(self):
		"""docstring for evaluate"""
		pass


