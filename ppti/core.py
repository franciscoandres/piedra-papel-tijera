class Core(object):

	def __init__(self):
		self._player = None
		self._machine = None
		self.result = None

	@property
	def player(self):
		return self._player

	@player.setter
	def player(self, value):
		self._player = value

	@property
	def machine(self):
		return self._machine

	@machine.setter
	def machine(self, value):
		self._machine = value

	def get_result(self):

		if self.player == "piedra" and self.machine == "tijera":
			self.result = True
		elif self.player == "tijera" and self.machine == "papel":
			self.result = True
		elif self.player == "papel" and self.machine == "piedra":
			self.result = True

		if self.machine == "piedra" and self.player == "tijera":
			self.result = False
		elif self.machine == "tijera" and self.player == "papel":
			self.result = False
		elif self.machine == "papel" and self.player == "piedra":
			self.result = False

		if self.player == "piedra" and self.machine == "piedra":
			self.result = None
		elif self.player == "tijera" and self.machine == "tijera":
			self.result = None
		elif self.player == "papel" and self.machine == "papel":
			self.result = None


		return self.result