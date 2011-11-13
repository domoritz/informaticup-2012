import copy
import random
import math

class PositionCities:

	def __init__(self, distances):
		self.distances = distances
		self.borderX = 800
		self.borderY = 600
		self.positions = []

	def optimize(self):
		random.seed(18577)
		
		for i in range(0, len(self.distances)):
			self.positions.append([random.randint(0, 1000), random.randint(0, 1000)])
		print self.positions

		temperature = 50
		iterations = 5
		operations = 3
		maxMove = 10

		while temperature > 0:
			for i in range(0, iterations):
				prevCost = self.evaluate()
				prevPositions = copy.deepcopy(self.positions)

				for j in range(0, operations):
					cityIndex = random.randint(0, len(self.distances)-1)
					self.positions[cityIndex][0] += random.randint(0, maxMove) - maxMove / 2
					self.positions[cityIndex][1] += random.randint(0, maxMove) - maxMove /2
				
				newCost = self.evaluate()
				deltaCost = newCost - prevCost

				if deltaCost > 0:
					if random.random >= 2.71 ** (-deltaCost / temperature):
						self.positions = prevPositions
			temperature -= 1

		maxX = 0
		maxY = 0
		for i in range(0, len(self.positions)):
			maxX = max(maxX, self.positions[i][0])
			maxY = max(maxY, self.positions[i][1])

		minX = maxX
		minY = maxY
		for i in range(0, len(self.positions)):
			minX = min(minX, self.positions[i][0])
			minY = min(minY, self.positions[i][1])
		
		maxX = 0
		maxY = 0
		for i in range(0, len(self.positions)):
			self.positions[i][0] -= minX
			self.positions[i][1] -= minY
			maxX = max(maxX, self.positions[i][0])
			maxY = max(maxY, self.positions[i][1])

		maxX = float(self.borderX) / maxX
		maxY = float(self.borderY) / maxY
		for i in range(0, len(self.positions)):
			self.positions[i][0] *= maxX
			self.positions[i][1] *= maxY
			
	def evaluate(self):
		cost = 0
		
		for city1 in range(0, len(self.positions)):
			for city2 in range(0, len(self.positions)):
				graphDistance = (self.positions[city1][0] - self.positions[city2][0]) ** 2 + (self.positions[city1][1] - self.positions[city2][1]) ** 2
				graphDistance = math.sqrt(graphDistance)
				cost += abs(self.distances.getDistance(city1, city2) - graphDistance)
				cost += 1 / max(0.01, graphDistance)	
		return cost

	def debugPrint(self):
		print "Position of cities:"
		for city in self.positions:
			print city
