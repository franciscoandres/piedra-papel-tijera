class Car(object):

	def __init__(self):
		self._model = None

	@property
	def model(self):
		print "Property"
		return self._model

	@model.setter
	def model(self, value):
		print "Setter"
		self._model = value

obj = Car()
print obj.model 
print obj.model = "Tesla S"


