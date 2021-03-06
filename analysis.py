from __future__ import print_function
import random
from pprint import pprint, pformat

from program.dataParser import DataParser
from program.genetic import Genetic
from program.clingo import Clingo
import logging
from helpers.output import ShoppingTourLogger
import sys

logging.setLoggerClass(ShoppingTourLogger)
logger = logging.getLogger('shoppingtour')
logger.setLevel(logging.WARN)
formatter = logging.Formatter("%(relativeCreated)s %(name)s %(levelname)s: %(message)s")
stderrHandler = logging.StreamHandler(sys.stderr)
stderrHandler.setFormatter(formatter)
logger.addHandler(stderrHandler)



oprint = print

n=8
if len(sys.argv) > 1:
	n = int(sys.argv[1])
k=10
if len(sys.argv) > 2:
	k = int(sys.argv[2])
distRange = [10,100]
ddensity = 0.3

def value():
	if (random.random() > ddensity):
		return None
	else:
		return random.randint(distRange[0],distRange[1])

def generateDistances(io):
	print = lambda *args, **kwargs: oprint(*args, file=io, **kwargs)
	a = [[value() for x in range(k)] for z in range(k)]

	print("Fahrtkosten", end='')
	for x in range(k):
		print(", g"+str(x), end='')
	print('')
	for i in range(k):
		print("g"+str(i), end='')
		for j in range(k):
			if i==j:
				a[j][i] = 0
			a[i][j] = a[j][i]
			if a[i][j] != None:
				print(",",a[i][j], end='')
			else:
				print(",", end='')
		print()


priceRange = [5,20]
variability = 0.2
pdensity = 0.15
sigma = 0.5
numberRange = [1,3]

def price(median):
	if (random.random() > pdensity):
		return None
	else:
		price = random.gauss(median,sigma)
		return abs(round(price,2))

def generatePrices(io):
	print = lambda *args, **kwargs: oprint(*args, file=io, **kwargs) 
	medianPrices = [random.randint(priceRange[0],priceRange[1]) for x in range(n)]
	pricesArray = [[price(medianPrices[z]) for x in range(k)] for z in range(n)]

	print("Artikel\Geschaeft,Menge", end='')
	for x in range(1,k):
		print(", g"+str(x), end='')
	print('')
	for i in range(n):
		line = "a"+str(i)
		line += ", "+str(random.randint(numberRange[0],numberRange[1]))
		if not filter(lambda s: s is not None, pricesArray[i]): # no price
			pricesArray[i][random.randint(0, len(pricesArray[i])-1 )] = abs(round(random.gauss(medianPrices[i], sigma), 2))
		oprint(pricesArray[i])
		for j in range(1,k):
			if pricesArray[i][j]:
				line +=  "," + str(round(pricesArray[i][j], 2))
			else:
				line += ","
		print(line)

print('n={0}, k={1}'.format(n, k))

import io

distancesIO = io.BufferedRandom(io.BytesIO())
pricesIO = io.BufferedRandom(io.BytesIO())

generatePrices(pricesIO)
generateDistances(distancesIO)

parser = DataParser()
dataInstance = parser.readInstance(pricesIO, distancesIO)

pprint(dataInstance.prices.data)
pprint(dataInstance.distances.data)

import time
now = time.time

clingo = Clingo(dataInstance)
clingoSolutions = []
print("starting clingo")
clingoStart = now()

for solution in clingo.generate():
	clingoSolutions.append((now(), solution))

if len(clingoSolutions) == 0:
	exit(1)

genetic = Genetic(dataInstance)
geneticSolutions = []
print("starting genetic")
geneticStart = now()
oldSolution = None

for solution in genetic.generate():
	if oldSolution != solution:
		geneticSolutions.append((now(), solution))
		oldSolution = solution

print("analysis")

minCosts = None
for i in xrange(len(clingoSolutions)):
	solution = clingoSolutions[i][1]
	costs = dataInstance.calculateExpenses(solution) + dataInstance.calculateSpendings(solution)
	if minCosts is None or costs < minCosts:
		minCosts = costs
	clingoSolutions[i] = (clingoSolutions[i][0] - clingoStart, costs)

for i in xrange(len(geneticSolutions)):
	solution = geneticSolutions[i][1]
	costs = dataInstance.calculateExpenses(solution) + dataInstance.calculateSpendings(solution)
	geneticSolutions[i] = (geneticSolutions[i][0] - geneticStart, costs)

print('clingo')
for solution in clingoSolutions:
	print(round(solution[0], 4), round(solution[1]/minCosts,4), sep=': ')
print('genetic')
for solution in geneticSolutions:
	print(round(solution[0], 4), round(solution[1]/minCosts,4), sep=': ')
