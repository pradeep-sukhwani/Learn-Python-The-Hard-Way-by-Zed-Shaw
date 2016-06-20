# assigning the varibles.
people = 30
cars = 40
trucks = 15

# here if/elif/else statement starts.
# here if statement will execute when cars is greater than people.
# or elif statement will execute when cars is less than people.
# or lastly else statement will execute when both of above is not possible.
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

# here if statement will execute when trucks is greater than cars.
# or elif statement will execute when trucks is less than cars.
# or lastly if both of above statement is not possible then else statement will execute.
if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

# here if statement will execute when trucks is greater than cars.
# or else statement will execute.
if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."