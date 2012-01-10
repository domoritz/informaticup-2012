from data.dataInstance import DataInstance
from program.algorithm import Algorithm
import subprocess

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
				"clingo": "clingo_prog/clingo"
			}
		else:
			self.options = options

		self.logger.pprint(problem.prices.data)
		self.logger.pprint(problem.distances.data)

		self.problem = problem

		self.prepare()

	def generate(self, solution = None):
		clingo = subprocess.Popen([self.options['clingo']] , stdout=subprocess.PIPE, stdin=subprocess.PIPE)
		clingo.stdin.write(self.costfile + self.graphfile)
		for f in self.files:
			clingo.stdin.write(self.costfile + self.graphfile + open(f).read())
		#print(clingo.stdout.read())
		stdout, stderr = clingo.communicate()
		print stdout
		yield [0,2,3]

	def prepare(self):
		"""prepares the calculation"""
		self.graphfile = ""
		self.costfile = ""

		#add nodes and products
		self.graphfile += "node(0..{n}).\n".format(n=self.problem.getNumberStores())
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
					self.costfile += "cost({product},{store},{cost}).\n".format(product=x,store=y+1,cost=cost) 

		print self.graphfile
		print self.costfile

		

