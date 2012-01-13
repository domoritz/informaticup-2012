from data.dataInstance import DataInstance
from program.algorithm import Algorithm
import subprocess
import re

class Clingo(Algorithm):
	""" 
	Uses clingo for solving the problem.
	Clingo is an asp solver by the university of potsdam. Website: http://potassco.sourceforge.net/
	"""

	files = ["clingo/ham.lp", "clingo/min.lp", "clingo/cost.lp", "clingo/graph.lp"]

	def __init__(self, problem, options = None):
		super(Clingo, self).__init__(problem)

		if options is None:
			self.options = {
				"clingo": "./clingo_prog/clingo",
                "clingoArgs": ""
			}
		else:
			self.options = options

		self.logger.pprint(problem.prices.data)
		self.logger.pprint(problem.distances.data)

		self.problem = problem

		self.prepare()

	def generate(self, solution = None):
		clingo = subprocess.Popen([self.options['clingo']] + self.options['clingoArgs'].split(" "), shell=False, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
		clingo.stdin.write(self.costfile + self.graphfile)
		for f in self.files:
			clingo.stdin.write(open(f).read())
		clingo.stdin.write(self.costfile + self.graphfile)
		clingo.stdin.close()

		while clingo.poll() is None or line != '':
			line = clingo.stdout.readline().strip("\n")
			self.logger.debug("Clingo: "+ line)
			solution = self.parseSolution(line)
			if solution:
				yield solution

	def cycle(self, lst, val, stop=None):
		d = dict(lst)
		stop = stop if stop is not None else val
		while True:
			yield val
			val = d.get(val, stop)
			if val == stop: break
	
	def parseSolution(self, line):
		"""
		parses the solution that come from clingo
			Answer: 3
			cycle(1,2) cycle(2,0) cycle(0,1) 
			Optimization: 8002
			OPTIMUM FOUND
		"""

		if re.match('^Answer: (\d)+',line):
			return None

		if re.match('^OPTIMUM FOUND$',line):
			self.logger.info(line)
			return None

		if re.match('^Optimization: (\d)+',line):
			return None

		if re.search('UNSATISFIABLE',line):
			self.logger.warn(line)
			return None

		if re.search('cycle',line):
			solution = [0]
			cycles = []
			cyclestrings = line.split(" ")
			for string in cyclestrings:
				match = re.match('^cycle\((\d+),(\d+)\)$', string)
				if match:
					cycles.append([int(match.group(1)),int(match.group(2))])

			solution = list(self.cycle(cycles, 0))

			return solution

		return None


	def prepare(self):
		"""prepares the calculation"""
		self.graphfile = ""
		self.costfile = ""

		#add nodes and products
		self.graphfile += "node(0..{n}).\n".format(n=self.problem.getNumberStores()-1)
		self.graphfile += "product(1..{n}).\n".format(n=len(self.problem.prices))

		#add expenses
		for x,row in enumerate(self.problem.distances.data):
			for y,cost in enumerate(row):
				if x < y:
					cost = int(cost*100)
					self.costfile += "expenses({x},{y},{cost}).\n".format(x=x,y=y,cost=cost)

		for x,row in enumerate(self.problem.prices.data):
			for y,cost in enumerate(row):
				if cost:
					cost = int(cost*100)
					self.costfile += "cost({product},{store},{cost}).\n".format(product=x+1,store=y+1,cost=cost) 

		#print self.graphfile
		#print self.costfile

		

