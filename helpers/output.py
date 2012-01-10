import logging
import pprint

class ShoppingTourLogger(logging.Logger):

	def __init__(self, name):
		super(ShoppingTourLogger, self).__init__(name)
		self.pp = pprint.PrettyPrinter(indent=4)

	def pprint(self, obj):
		self.debug("\n"+self.pp.pformat(obj))
