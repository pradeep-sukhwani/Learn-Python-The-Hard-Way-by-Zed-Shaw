print "You have a reached British library. You have 3 options:"
print "1. Pick a book of your choice and start reading it."
print "2. Rent a book of your choice and go back to home to read."
print "3. Leave the library because you didn't found your book of choice."

library = raw_input("> ")

if library == "1" or library == "2":
	print """
	You have 3 options:
	1. Comic Books.
	2. Science related books.
	3. Music related books.
	"""
	option = raw_input("> ")
	
	if option == "1":
		print "In comic books:"
		print "1. Batman"
		print "2. Spider-man"
		print "3. Superman"
		
		comic_books = raw_input("> ")
		if comic_books == "1":
			print "You will know about batman and his life."
		elif comic_books == "2":
			print "You will know about spider-man and his life."
		elif comic_books == "3":
			print "You will know about superman and his life."
		else:
			print "There is no other comic books available as of now."
	
	elif option == "2":
		print "In Science section:"
		print "1. Astronauts"
		print "2. Space Travel"
		print "3. Planets"
		
		science = raw_input("> ")
		if science == "1":
			print "You will know about life of astranauts."
		elif science == "2":
			print "You will know about space travels by NASA."
		elif science == "3":
			print "You will know about planets in our universe."
		else:
			print "There is no other topic available as of now."
	
	elif option == "3":
		print "In music section:"
		print "1. Instruments Music"
		print "2. Rock Music"
		print "3. Soft Music"
		
		music = raw_input("> ")
		if music == "1":
			print "You will know about instrument music."
		elif music == "2":
			print "You will know about rock music."
		elif music == "3":
			print "You will know about soft music."
		else:
			print "There is no other types of music available as of now."
	
	else:
		print "There is no other option available for you as of now."

else:
	print "You don't belong here go home and rest."