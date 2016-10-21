import random 
import core

options = ["piedra", "papel", "tijera"]

user = {
	"name": "",
	"option": None,
	"lifes": 3
}

machine = {
	"option": random.choice(options)
	#"option": "papel"
}

config = {
	"round_count": 1,
	"playing": True
}

user["name"] = raw_input("> Cual es tu nombre? ").title()
print "> %s elige bien..." % user["name"]

# The Loop
while config["playing"]:

	# Show round 
	print "Ronda {round_count} - Vidas [{lifes}]".format(round_count = config["round_count"], lifes = user["lifes"] ).center(40, "_")

	# Machine new option
	machine["option"] = random.choice(options)

	# Get the option, if doesnt match with the options on the list, get the option, repeat
	while not user["option"] in options:
		try:
			user["option"] = raw_input("> Elige Piedra, Papel o Tijera: ").lower()
		except ValueError: # CHECK THIS
			print "Por favor selecciona correctamente: "

	# Show the options
	print "Tu seleccion fue: %s" % user["option"].title()
	print "La maquina selecciono: %s " % machine["option"].title()

	# User and machine options
	result = core.compare_options(user["option"], machine["option"])

	if result == True:
		print "> Ganaste"

		# Reset the user option
		user["option"] = None
	elif result == False:
		print "> Perdiste"
		user["lifes"] -= 1

		# Reset the user option
		user["option"] = None
	elif result == None:
		print "> Empate"

		# Reset the user option
		user["option"] = None

	config["round_count"] += 1

	if user["lifes"] == 0:
		config["playing"] = False
		print "> Juego terminado!"

		