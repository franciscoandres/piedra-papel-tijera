import random 
import core

options = ["piedra", "papel", "tijera"]

user = {
	"name": "",
	"option": None,
	"lifes": 3,
	"result": {
		"rounds": 1,
		"wins": 0,
		"loses": 0,
		"ties": 0
	}
}

machine = {
	#"option": random.choice(options)
	"option": "papel"
}

config = {
	"playing": True
}

user["name"] = raw_input("> Cual es tu nombre? ").title()
print "> {name} elige bien...".format(name = user["name"])

# The Loop
while config["playing"]:

	# Show round
	print " "
	print "Ronda {round_count} - Vidas [{lifes}]".format(round_count = user["result"]["rounds"], lifes = user["lifes"] ).center(40, " ")

	# Get the option, if doesnt match with the options on the list, get the option, repeat
	while not user["option"] in options:
		try:
			user["option"] = raw_input("> Elige Piedra, Papel o Tijera: ").lower()
		except ValueError: # CHECK THIS
			print "Por favor selecciona correctamente: "

	# Machine new option
	#machine["option"] = random.choice(options)

	# Show the options
	print "Tu seleccion fue: {option}".format(option = user["option"].title())
	print "La maquina selecciono: {option} ".format(option = machine["option"].title())

	# User and machine options
	result = core.compare_options(user["option"], machine["option"])

	# Check the result
	if result == True:
		core.result_message(True, "Ganaste")

		# Reset the user option
		user["option"] = None
		user["result"]["wins"] += 1

	elif result == False:
		# Message
		core.result_message(False, "Perdiste")
		# -1 if you lost
		user["lifes"] -= 1
		# Reset the user option
		user["option"] = None
		user["result"]["loses"] += 1

	elif result == None:
		# Message
		core.result_message(None, "Empate")

		# Reset the user option
		user["option"] = None
		user["result"]["tie"] += 1
	# Round count
	user["result"]["rounds"] += 1

	#Finish the game
	if user["lifes"] == 0:
		config["playing"] = False
		user["result"]["rounds"] -= 1
		print "> Rondas: {0} | Ganaste: {1} | Perdiste: {2} | Empates: {3}".format(user["result"]["rounds"], user["result"]["wins"], user["result"]["loses"], user["result"]["ties"] )
		print "> Juego terminado!"

		