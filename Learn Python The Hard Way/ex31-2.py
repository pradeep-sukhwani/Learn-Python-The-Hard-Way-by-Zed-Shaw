print "You enter a dark room with 3 doors.  From which door do you want to go?"

door = raw_input("> ")

if door == "1":
	print "There's a gaint bear here eating a cheese cake. What do you do?"
	print "1. Take the cheese cake."
	print "2. Scream at the bear."
	print "3. Hit the bear with rod."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off.  Good job!"
	elif bear == "2":
		print "The bear eats off your legs off.  Good job!"
	elif bear == "3":
		print "The bear catches you first before you hit and makes you his food."
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello.  Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck.  Good job!"

elif door == "3":
	print "You saw lion eating meat."
	print """Here you have 3 option:
	1. Take the meat.
	2. Scream at the lion.
	3. Hit the lion with rod."""
	
	lion = raw_input("> ")
	
	if lion == "1" or lion == "2":
		print "Lion attacked you with its claws. You died!"
	else:
		print "This is the better step as lion ran away because you hit it with rod."

else:
	print "You stumble around and fall on a knife and die.  Good job!"