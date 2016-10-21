def compare_options(user, machine):
	if user == "piedra" and machine == "tijera":
		return True
	elif user == "tijera" and machine == "papel":
		return True
	elif user == "papel" and machine == "piedra":
		return True

	if machine == "piedra" and user == "tijera":
		return False
	elif machine == "tijera" and user == "papel":
		return False
	elif machine == "papel" and user == "piedra":
		return False
	# I dont know if return none will be an issue in the future...
	if user == "piedra" and machine == "piedra":
		return None
	elif user == "tijera" and machine == "tijera":
		return None
	elif user == "papel" and machine == "papel":
		return None


def result_message(value, text):
	if value == True:
		print " "
		print "*" * 40
		print text.center(40, " ")
		print "*" * 40
		print " "
	elif value == False:
		print " "
		print "/" * 40
		print text.center(40, " ")
		print "/" * 40
		print " "
	elif value == None:
		print " "
		print "%" * 40
		print text.center(40, " ")
		print "%" * 40
		print " "