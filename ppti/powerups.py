class PowerUps(object):
	
	def __init__(self):
		self.extraLife = {
			"name": "Vida!",
			"message": "> Obtienes vida extra!",
			"life": 1,
			"counter": 1
		}

	def show_name(self):
		return self.extra_life["name"]

	def show_message(self):
		return self.extra_life["message"]

	def extra_life(self):
		return int(self.extraLife["life"])

	def plus_counter(self):
		self.extraLife["counter"] += 1

	def reset_counter(self):
		self.extraLife["counter"] = 0