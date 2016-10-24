import random

class Machine(object):
	
	def __init__(self):
		self._option = None

	@property
	def option(self):
		return self._option

	@option.setter
	def option(self, options):
		self._option = random.choice(options)

	def reset_option(self):
		self._option = None
