import core
import player
import machine
import score

playing = True
options = ["piedra", "papel", "tijera"]

player = player.Player()
machine = machine.Machine()
match = core.Core()

while playing:

	while not player.option in options:
		try:
			player.option = raw_input("Elige Piedra, Papel o Tijera: ")
			machine.option = options
		except ValueError:
			print "Error"

	match.player = player.option
	match.machine = machine.option

	print "Tu eleccion fue: {}".format(match.player.title())
	print "La maquina selecciono: {}".format(match.machine.title())

	result = match.get_result()

	if result == True:
		print "Ganaste"
	elif result == False:
		print "Perdiste"
	elif result == None:
		print "Empate"


	playing = False

	

