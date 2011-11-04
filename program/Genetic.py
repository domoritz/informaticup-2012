from data.DataInstance import DataInstance
from program.Algorithm import Algorithm
import random
import pprint

class Genetic(Algorithm):
    """ Genetic algorithm """

    def __init__(self, problem, options = None):
        super(Genetic, self).__init__(problem)

        if options is None:
            self.options = {
                "popsize":1,
                "childrenGroup": 2,
                "mutation": 3,
                "maxGenerations": 100,
                "seed": 1
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
        if False:
            yield None   

    def brew(self):
        """generate a population"""
        numberCities = self.problem.getNumberStores()
        self.population = [[[random.randint(1,numberCities-y) for y in range(numberCities)], 0] for x in range(self.options["popsize"])]
        for individuum in self.population:
            individuum[1] = self.evaluate(individuum[0])
            pprint.pprint(self.population)


    def evaluate(self, array):
        """docstring for evaluate"""
        solution = []
        shops = range(self.problem.getNumberStores())
        for position in array:
            solution.append(shops.pop(position-1))
        return self.problem.calculateCost(solution)


