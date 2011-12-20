import logging
import pprint

class ShoppingTourLogger(logging.Logger):

	def __init__(self, name):
		super(ShoppingTourLogger, self).__init__(name)
		self.pp = pprint.PrettyPrinter(indent=45)

	def pprint(self, obj):
		self.debug(self.pp.pformat(obj))
