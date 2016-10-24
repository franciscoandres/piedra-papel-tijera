class Player(object):

	def __init__(self):
		self._name = ""
		self._option = None
		self._life = 3

	@property
	def name(self):
		return self._name.title()

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def option(self):
		if self._option == None:
			return self._option
		else:
			return self._option.lower()

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