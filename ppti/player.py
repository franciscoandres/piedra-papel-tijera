class Player(object):

	def __init__(self):
		self._option = None

	@property
	def option(self):
		return self._option

	@option.setter
	def option(self, value):
		self._option = value