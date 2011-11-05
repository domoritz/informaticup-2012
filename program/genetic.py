from data.dataInstance import DataInstance
from program.algorithm import Algorithm
import random
import pprint

class Genetic(Algorithm):
    """ Genetic algorithm """

    def __init__(self, problem, options = None):
        super(Genetic, self).__init__(problem)

        if options is None:
            self.options = {
                "popsize":10,
                "childrenGroup": 2,
                "mutation": 3,
                "maxGenerations": 100,
                "seed": 42
            }
        else:
            self.options = options

        pprint.pprint(problem.prices.data)
        pprint.pprint(problem.distances.data)

        self.problem = problem
        self.population = []
        random.seed(self.options["seed"])

    def generate(self, solution = None):
        """creates a solution and yields it as a list 
        of numbers which stand for the shops
        i.e. [4,6,2,3,1,5]
        this means, solve is a generator
        """
        self.brew()
        self.sort()

        if True:
            print("\nGenetic Algorithm\n===============")
            print("First population: ")
            pprint.pprint(self.population)

        if False:
            yield None 

    def brew(self):
        """generate a population"""
        numberCities = self.problem.getNumberStores()
        self.population = [[[random.randint(1,numberCities-y) for y in range(numberCities)], 0] for x in range(self.options["popsize"])]
        for individuum in self.population:
            individuum[1] = self.evaluate(individuum[0])


    def evaluate(self, array):
        """docstring for evaluate"""
        solution = []
        shops = range(self.problem.getNumberStores())
        for position in array:
            solution.append(shops.pop(position-1))
        return self.problem.calculateCost(solution)

    def sort(self):
        """sorts the population by cost"""
        self.population.sort(cmp = lambda a,b: cmp(a[1],b[1]))

    def crossover(self, arr1, arr2, cut):
        """does the crossover at the position cut (right before it)
        ie: [1,2,3,4] cut 2 menas between the 2 and 3"""
        return arr1[:cut]+arr2[cut:]
