class Player(object):

	def __init__(self):
		self._option = None
		self._life = 3

	@property
	def option(self):
		return self._option

	@option.setter
	def option(self, value):
		self._option = value

	def reset_option(self):
		self._option = None

	@property
	def life(self):
		return self._life

	@life.setter
	def handle_life(self, item):
		# var_1, var_2 = (param_1, param_2) <- tuple
		operator, value = item
		if operator == "+":
			self._life += value
		elif operator == "-":
			self._life -= value