# -*- coding: utf-8 -*- 

import core
import player
import machine
import score

playing = True
options = ["piedra", "papel", "tijera"]

player = player.Player()
machine = machine.Machine()
match = core.Core()

while not player.name:
	player.name = raw_input("Nombre: ")

while playing:

	while not player.option in options:
		try:
			player.option = raw_input("> Elige Piedra, Papel o Tijera: ")
			machine.option = options
		except ValueError:
			print "Error"

	match.player = player.option
	match.machine = machine.option

	print "> {}: {} | Maquina: {}".format(player.name, match.player.title(), match.machine.title())

	result = match.get_result()

	if result == True:
		print "> Ganaste"
	elif result == False:
		player.handle_life = ("-", 1)
		print "> Perdiste"
	elif result == None:
		print "> Empate"

	print "> ¡!: Te quedan {} vidas".format(player.life)
	player.reset_option()
	machine.reset_option()

	if player.life == 0:
		playing = False
		print "> Juego terminado!"
