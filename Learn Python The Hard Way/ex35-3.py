from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def dark_tunnel():
	print "You have entered in a dark tunnel now."
	print "There is a flambeau on the wall."
	take_flambeau = False
	
	while True:
		choice = raw_input("> ")
	
		if choice == "take flambeau" and not take_flambeau:
			print "You can see the door in front of you."
			take_flambeau = True
		elif choice == "open door" and take_flambeau:
			gold_room()
		else:
			print "I got no idea what that means?"
	
def cthulhu_room():
	print "Here you can see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or you want to eat your head?"
	
	choice = raw_input("> ")
	
	if "flee" == choice:
		bear_room()
	else:
		dead("You go insane and Cthulhu pissed off your head.")
		
def bear_room():
	print "You flee from Cthulhu room and land to bear room."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can now go through it."
			bear_moved = True
		elif choice == "open door" and bear_moved:
			dark_tunnel()
		else:
			print "I got no idea what that means."

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "Where is a door in front of you"
	print "Do you want to go in?"
	
	choice = raw_input("> ")
	
	if choice == "yes":
		cthulhu_room()
	else:
		start()
		
start()