from data.dataInstance import DataInstance
from program.algorithm import Algorithm
import random

class Genetic(Algorithm):
	""" 
	Genetic algorithm 
	"""
	#TODO schneller machen
	#TODO messen wie schnell es geht
	#TODO parameter besser anpassen

	def __init__(self, problem, options = None):
		"""
		options:
			popsize:		size of the population (higher is better but slower)
			childrenGroup:	number of indviduals to be choosen for replacement 
							with new children from 2 the number of parents
			mutation:		probability of mutuation (higher means faster but less accurate)
			shortening:		probability of shortening solution. 
			maxGenerations: maximum number of generations to be crated by python 
							generator (higher better but needs more time).
			seed:			seed for python random. If this stays the same, the result will 
							always be the same. Use None in order to get random.
		"""
		super(Genetic, self).__init__(problem)

		if options is None:
			self.options = {
				"popsize":25,
				"childrenGroup": 3,
				"mutation": 50,
				"shortening": 20,
				"maxGenerations": 100,
				"seed": 42
			}
		else:
			self.options = options

		self.logger.pprint(problem.prices.data)
		self.logger.pprint(problem.distances.data)

		self.problem = problem
		self.population = []
		random.seed(self.options["seed"])
		self.length = 0
	
	def __str__(self):
		str = ""
		for index,individual in enumerate(self.population):
			str += ("{0:3d}: {1} = {2} {3}\n").format(index,individual[0],individual[1],self.helperTransform(individual[0]));
		return str

	def generate(self, solution = None):
		"""creates a solution and yields it as a list 
		of numbers which stand for the shops
		i.e. [4,6,2,3,1,5]
		this means, solve is a generator
		"""
		self.brew()
		self.sort()

		self.logger.debug("\nGenetic Algorithm\n=================")
		self.logger.debug("First population: ")
		self.logger.debug(self)

		for i in range(self.options['maxGenerations']):
			self.logger.debug('Generation no: {num}\n================='.format(num = i))

			#how to make children
			for p in range(self.options['childrenGroup']):
				#TODO nicht nur direkte nachbar paaren lassen
				indiv0 = self.population[2*p][0]
				indiv1 = self.population[2*p+1][0]
																						#not first and not last for cut
				self.population[-p-1][0] = self.crossover(indiv0, indiv1,random.randint(1,(len(indiv0)+len(indiv1))/2-1))
				self.population[-p-1][1] = self.evaluate(self.population[-p-1][0])

			# make mutation
			for x in range(self.options['popsize'] - self.options['childrenGroup']+1, self.options['popsize']):
				if self.options['mutation'] >= random.randint(0,100):
					self.population[x][0] = self.mutuate(self.population[x][0])
					self.population[x][1] = self.evaluate(self.population[x][0])
				if self.options['shortening'] >= random.randint(0,100) and len(self.population[x][0]) > 1:
					self.population[x][0] = self.shorten(self.population[x][0])
					self.population[x][1] = self.evaluate(self.population[x][0])
			
			#sort by cost/performance
			self.sort()

			self.logger.debug(self)
			
			# yield the best solution so far
			yield self.helperTransform(self.population[0][0]),self.population[0][1]

	def brew(self):
		"""generate a population"""
		numberCities = self.problem.getNumberStores()
		self.length = numberCities
		self.population = [[[random.randint(0,numberCities-y-1) for y in range(numberCities)], 0] for x in range(self.options["popsize"])]
		for individual in self.population:
			individual[1] = self.evaluate(individual[0])

	def helperTransform(self, array):
		"""generates solution format out of internal format"""
		solution = []
		shops = range(self.problem.getNumberStores())
		for position in array:
			solution.append(shops.pop(position))
		return solution

	def evaluate(self, array):
		"""evaluates an individual and calculates a solution's cost/performance"""
		return self.problem.calculateCost(self.helperTransform(array))

	def sort(self):
		"""sorts the population by cost/performance"""
		self.population.sort(cmp = lambda a,b: self.compare(a[1],b[1]))

	def compare(self, a, b):
		if not a:
			return 1
		if not b:
			return -1
		return cmp(a,b)

	def crossover(self, arr1, arr2, cut):
		"""does the crossover at the position cut (right before it)
		ie: [1,2,3,4] cut 2 means between the 2 and 3"""
		return arr1[:cut]+arr2[cut:]

	def mutuate(self, solution):
		"""mutuates an individual"""
		#TODO sicherstellen, dass nur eine aenderung vorgenommen wird
		length = len(solution)
		whichGene = random.randint(0,length - 1)
		solution[whichGene] = random.randint(0,(length - 1)-whichGene)
		return solution

	def shorten(self, solution):
		"""
		shortens a solution and remove one random store
		Uses a special algorithm in order to just remove one
		store and keep the rest untouched.
		"""
		self.logger.debug('{0}, {1}'.format(solution, self.helperTransform(solution)))
		length = len(solution)
		whichGene = random.randint(0,length - 1)
		former = solution.pop(whichGene)
		self.logger.debug('{0}, {1}'.format(whichGene,former))
		for i in range(whichGene, length-1):
			if solution[i]>=former:
				solution[i]+=1
			former-=1
		self.logger.debug('{0}, {1}'.format(solution, self.helperTransform(solution)))
		return solution
