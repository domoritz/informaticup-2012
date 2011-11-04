from data.DataInstance import DataInstance
from program.Algorithm import Algorithm
import random
import pprint

class Genetic(Algorithm):
    """ Genetic algorithm """

    def __init__(self, data, options = None):
        super(Genetic, self).__init__(data)

        if options is None:
            self.options = {
                "popsize":20,
                "childrenGroup": 2,
                "mutation": 3,
                "maxGenerations": 100,
                "seed": 1
            }
        else:
            self.options = options

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
        numberCities = 10
        self.population = [[random.randint(0,numberCities-y) for y in range(numberCities)] for x in range(self.options["popsize"])]
        pprint.pprint(self.population)


    def evaluate(self):
        """docstring for evaluate"""
        pass


