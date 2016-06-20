from sys import exit

def girl_room():
	print "Here you saw a girl is lying on the floor.\n"
	pick_up = False
	walk = False
	open_door = False
	go_near = False
	help = False
	while True:
		choice = raw_input("Ichabod Crane: ")
		
		if choice == "help" and not help:
			print "This is a room with the door on the right side and a girl is lying on the floor."
			print "Black Magic: No"
			print "Suspious Thing: No\n"
			help = True
		elif choice == "go near" and help and not go_near:
			print "Its Abbhi.\n"
			go_near = True
		elif choice == "pick up" and help and go_near and not pick_up:
			print "Carry her out of the house.\n"
			pick_up = True
		elif choice == "walk" and help and go_near and pick_up and not walk:
			print "You have reached the door.\n"
			walk = True
		elif choice == "open door" and help and go_near and pick_up and walk and not open_door:
			print "You are now out of the house."
			print "Now blow up the house with C4 that you have.\n"
			open_door = True
		elif choice == "blow-up" and help and go_near and pick_up and walk and open_door:
			print "Boom!! Boom!! BOOM!!"
			print "You have successfully blew up the house."
			print "You have successfully rescue Abbhi"
			print "You won.\n"
			exit(0)
		else:
			print "I got no idea what that means?\n"

def lion_room():
	print "Here you saw a pride of lions.\n"
	help = False
	count = False
	hypnotize = False
	move = False
	walk = False
	open_door = False
	close_door = False
	
	
	while True:
		choice = raw_input("Ichabod Crane: ")
		if choice == "help" and not help:
			print "This room is full of Lions with a door on the left side. Be Carefull!!"
			print "Black Magic = No"
			print "Suspious Thing = Yes! These Lions can smell you and hear you if make any noise."
			print "Lions Weakness: You can control them by hypnotizing them. And move all at one corner.\n"
			help = True
		elif choice == "count" and help and not count:
			print "Their are 12 Lions.\n"
			count = True
		elif choice == "hypnotize them" and help and count and not hypnotize:
			print "You have successfully hypnotize all lions.\n"
			hypnotize = True
		elif choice == "move all to right side" and help and count and hypnotize and not move:
			print "Lions are on right side."
			print "Now you can go.\n"
			move = True
		elif choice == "walk" and help and count and hypnotize and move and not walk:
			print "You have reached the door.\n"
			walk = True
		elif choice == "open door" and help and count and hypnotize and move and walk and not open_door:
			print "You have reached in the next room. Now close the door else lions will eat you.\n"
			open_door = True
		elif choice	== "close door" and help and count and hypnotize and move and walk and open_door and not close_door:
			print "You have successfully close the door.\n"
			close_door = True
			girl_room()
		else:
			dead("Lion attack you with claws and you're being eaten by its group.\n") 

def mummies_room():
	print "Here you saw mummies lying on the floor.\n"
	help = False
	light = False
	hit = False
	move = False
	open_door = False
	
	while True:
		choice = raw_input("Ichabod Crane: ")
		if choice == "help" and not help:
			print "This room is full of mummies, scrapes likes papers, waste, fire pot, Lighter and with a door on the left side."
			print "Black Magic: No."
			print "Suspious Thing: Yes. They can't see you but they can hear you if you make any noice."
			print "Only one way to kill them is set up the fire. They will burned to death."
			print "Now light the fire pot.\n"
			help = True
		elif choice == "light" and help and not light:
			print "You have successfully light the fire pot."
			print "Now hit them with your fire pot. So they get burned to death.\n"
			light = True
		elif choice == "hit" and help and light and not hit:
			print "Mummies are burning..."
			print "Mummies are burned to death."
			print "Now you can move towards the door.\n"
			hit = True
		elif not hit:
			dead("You're dead because you are not old enought to fight with mummies.\n")
		elif choice == "move" and help and light and hit and not move:
			print "You have reached the door.\n"
			move = True
		elif choice == "open door" and help and light and hit and move and not open_door:
			print "You've reached in the next room.\n"
			open_door = True
			lion_room()
		else:
			print "I got no idea what that means?\n"
			
def alien_room():
	print "Here you saw something strange. You can't recognise what is that thing?\n"
	help = False
	open = False
	take = False
	wear = False
	look_around = False
	grenade = False
	go_near = False
	check = False
	walk = False
	open_door = False
	
	while True:
		choice = raw_input("Ichabod Crane: ")
		if choice == "help" and not help:
			print "Here in this room you saw aliens."
			print "This room has a door just behind the alien which is on right side."
			print "Black Magic: Yes. They can control you."
			print "Suspious Thing: Yes. They can also hear you if you make any noise."
			print "Behind you their is a wardrobe open it to see if their is something valuable?\n"
			help = True
		elif choice == "open" and help and not open:
			print "Here you see an alien helmet and 5 grenades."
			print "Hopefully this will be enough to kill them!!"
			print "Take them.\n"
			open = True
		elif choice == "take" and help and open and not take:
			print "You have taken 5 grenades and an alien helmet."
			print "Wear an alien helmet so that they can't control you.\n"
			take = True
		elif choice == "wear" and help and open and take and not wear:
			print "You have wear an alien helmet."
			print "Now first have a look around where to throw grenades?\n"
			wear = True
		elif choice == "look around" and help and open and take and wear and not look_around:
			print "You saw 2 aliens at right side and just ahead their is another 2 aliens."
			print "And their is another alien on the right side guarding the door."
			print "Their is another alien which is in the corner to the left side standing with another alien."
			print "Thow two grenades at the right side, one grenade at the middle and two at the left side corner."
			print "So that it will destroy all materials and hopefully will kill the aliens.\n"
			look_around = True
		elif not look_around:
			dead("Aliens had controlled your mind and you're dead.\n")

		elif choice == "throw grenades" and help and open and take and wear and look_around and not grenade:
			print "Fire in the hole!!"
			print "Boom Boom Boom Boom BOOOM!!" 
			print "It looks like you've killed the aliens, but check it go near them.\n"
			grenade = True
		elif choice == "go near" and help and open and wear and look_around and grenade and not go_near:
			print "You have reached near the alien check it.\n"
			go_near = True
		elif choice == "check" and help and open and wear and look_around and grenade and go_near and not check:
			print "Congrats! You have successfully killed the aliens."
			print "Now walk towards the door.\n"
			check = True
		elif choice == "walk" and help and open and wear and look_around and grenade and go_near and check and not walk:
			print "You have reached the door."
			print "Now open the door.\n"
			walk = True
		elif choice == "open door" and help and open and wear and look_around and grenade and go_near and check and walk and not open_door:
			print "You have reached in the next room.\n"
			open_door = True
			mummies_room()
		else:
			print "I got no idea what that means?\n"

def illusion_room():
	print "Here you saw your Abbie just fit and healthy as she was before.\n"
	help = False
	light = False
	move = False
	open_door = False
	close_door = False
	
	while True:
		choice = raw_input("Ichabod Crane: ")
		if choice == "help" and not help:
			print "This room has so many wastes like papers, match box, tiffin, bottles, candles, etc with a door behind Abbhi."
			print "Wait a minute, I don't feel something good here, Its trap.."
			print "This can't be Abbie."
			print "Black Magic: Yes! She is an evil spirit in the face of Abbie."
			print "Suspious Thing: Yes! She want to capture you for the rest of your life."
			print "Evil Spirit is always afriad of fire. Light the candles, papers. So spirit will fall back.\n"
			help = True
		elif choice == "light" and help and not light:
			print "You have successfully light the papers and candles"
			print "And that evil spirit is going back."
			print "Now move towards the door but make sure keep distance between you and spirit.\n"
			light = True
		elif not light:
			dead("Evil Spirit had entered in your body since you didn't light the candles, so you're dead!\n")
		elif choice == "move" and help and light and not move:
			print "Now you have reached the door."
			print "Now open the door without turning back."
			print "By taking your one hand to the knob of the door.\n"
			move = True
		elif choice == "open door" and help and light and move and not open_door:
			print "You have reached in the next room."
			print "Now close the door because evil spirit will kill you.\n"
			open_door = True
		elif choice == "close door" and help and light and move and open_door and not close_door:
			print "You have successfully closed the door.\n"
			close_door = True
			alien_room()
		else:
			dead("Evil spirit has entered in your body and you're dead!\n")

def poison_room():
	print "Here you saw a book lying the middle of the room.\n"
	help = False
	walk = False
	look_back_around = False
	open = False
	help_again = False
	go = False
	drink = False
	move = False
	open_door = False
	
	while True:
		choice = raw_input("Ichabod Crane: ")
		if choice == "help" and not help:
			print "This room only contains a mysterious book and door."
			print "The door will only open if you open the book."
			print "Black Magic: Yes, but can't say anything about the book."
			print "Suspious Thing: Want to kill you."
			print "Now walk towards the book.\n"
			help = True
		elif choice == "walk" and help and not walk:
			print "You've reached near the book."
			print "Now look to the book and noticed anything about unusual.\n"
			walk = True
		elif choice == "look" and help and walk and not look_back_around:
			print "The Book has hard cover with a title"
			print "The title of book says:"
			print "Death"
			print "By: Abbhi"
			print "Notice that the book may have something related to abbie!"
			print "Now open the book.\n"
			look_back_around = True
		elif choice == "open" and help and walk and look_back_around and not open:
			print "A strange gas is coming out from the book."
			print "Once again press help for more information on gas.\n"
			open = True
		elif choice == "help again" and help and walk and look_back_around and open and not help_again:
			print "This book contains a poisonous gas."
			print "This is Beijing Cocktail poison in a gas form. It is very dangerous."
			print "It will cause you weakness, blurred vision and chest pain."
			print "Approximate time to live is 10 mins."
			print "Treatment: Their is table on the right side of door. Go their.\n"
			help_again = True
		elif not help_again:
			print "I got no idea what that means?\n"
		elif choice == "go" and help and walk and look_back_around and open and help and not go:
			print "You have reached near the table."
			print "Now drink the blood of dragon. This will kill the poisonous gas which inside your body.\n"
			go = True
		elif choice == "drink" and help and walk and look_back_around and open and help and go and not drink:
			print "You are now fit and fine as before."
			print "Now move towards the door.\n"
			drink = True
		elif not drink:
			dead("You are dead because of the poison.\n")
		elif choice == "move" and help and walk and look_back_around and open and help and go and drink and not move:
			print "You've reached near the door."
			print "Now open the door.\n"
			move = True
		elif choice == "open door" and help and walk and look_back_around and open and help and go and drink and move and not open_door:
			print "You've reached in the next room.\n"
			open_door = True
			illusion_room()
		else:
			print "I got no idea what that means?\n"

def free_room():
	print "Here you saw an chair with skeleton on it and a door behind the table.\n"
	help = False
	move = False
	open_door = False
	
	while True:
		choice = raw_input("Ichabod Crane: ")
		if choice == "help" and not help:
			print "The skeleton looks of woman."
			print "Let it go."
			print "Now move towards the door that is behind the table.\n"
			help = True
		elif choice == "move" and help and not move:
			print "You've reached near the door."
			print "No open the door.\n"
			move = True
		elif choice == "open door" and help and move and not open_door:
			print "You've reached in the next room.\n"
			open_door = True
			poison_room()
		else:
			print "I got no idea what that means?\n"

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
	print "Once upon a time their was a boy name 'Ichabod Crane' who loves a girl name 'Grace Abigail' known by 'Abbie'. One"
	print "day they were playing hide and seek and the girl has to hide somewhere so at a nearby distance she saw a house and"
	print "she thought it would be nice place to hide. As the front door was locked so she climbed up on that door and she jumped"
	print "inside and she felt and she was also bleeding and she drop one of her earings in front of the gate on the inside side."
	print "Ichabod was looking for her but he didn't find her, after some time he also found that house, he went near to the"
	print "front and he looked at one of her earings, so he climbed up he jumbed in and picked up her earings.\n"
	print "Now you see a door in front of you."
	print "Go there.\n"
	
	go = False
	open_door = False
	
	while True:
		choice = raw_input("Ichabod Crane: ")
		if choice == "go" and not go:
			print "You've reached the door."
			print "Now open the door.\n"
			go = True
		elif choice == "open door" and go and not open_door:
			print "You are now inside the haunted house."
			print "Carefull Bats are coming out."
			print "Remember you can get vibes by pressing 'help' and you can control minds.\n"
			open_door = True
			free_room()
		else:
			print "I got no idea what that means?\n"
start()