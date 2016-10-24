# -*- coding: utf-8 -*- 

import core
import player
import machine
import powerups

playing = True
options = ["piedra", "papel", "tijera"]

player = player.Player()
machine = machine.Machine()
match = core.Core()

life = powerups.PowerUps()

while not player.name:
	player.name = raw_input("Jugador: ")

while playing:

	print "_" * 40
	print "> Jugador: [{}] | Vidas: [{}]".format(player.name, player.life)

	while not player.option in options:
		try:
			player.option = raw_input("> Elige Piedra, Papel o Tijera: ")
			machine.option = options
		except ValueError:
			print "Error"

	match.player = player.option
	match.machine = machine.option

	print "> {}: {} | Maquina: {}".format(player.name, match.player.title(), match.machine.title())

	print "_" * 40

	result = match.get_result()

	if result == True:

		counter = life.extraLife["counter"]
		print counter
		life.plus_counter()

		if counter == 3:
			player.handle_life = ("+", life.extra_life())
			print life.extraLife["message"]

		print "> Ganaste"

	elif result == False:
		player.handle_life = ("-", 1)

		life.reset_counter()
		print "> Perdiste"
	elif result == None:

		life.reset_counter()
		print "> Empate"

	print "> ¡!: Te quedan {} vidas".format(player.life)
	player.reset_option()
	machine.reset_option()

	if player.life == 0:
		playing = False
		print "> Juego terminado!"
