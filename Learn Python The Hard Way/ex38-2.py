#declare varible ten_things
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# print statement
print "Wait there are not 10 things in that list. Let's fix that."

# declare variable stuff. ten_things.split(' ') means 
# to call split function on ten_things to make them 
# split with single notation.
# split(ten_things) means call split function
# with argument ten_things

stuff = ten_things.split(' ')

# create list with a varible name more_stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# used while loop.
# used len function on stuff
# declare variable next_one, more_stuff.pop()
# means call pop function on more_stuff means
# to remove the given items from the list and return it .
# pop(more_stuff) means call pop function with
# argument more_stuff.
# print statement with strings and variable.
# stuff.append(next_one) means call append function
# on stuff to increse the number of things in list.
# print statement with decimal format
while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

# print statement with varible.	
print "There we go: ", stuff

# print statement
print "Let's do some things with stuff."

# print statement with variable(which is now a list)
# with item no. 2 and index no.1
# with last item i.e. 10 and index no. -1
# stuff.pop() means call pop function on stuff means
# to remove the given items from the list and return it.
# pop(stuff) means call pop function with
# argument stuff. This will print the item which has
# last index no.
# ' '.join(stuff) this will join the all the thing in
# stuff
# '#'.join(stuff[3:5]) this will extracts the slice
# from element 3 to element 4 meaning it does not include
# element 5. It is similar to range(3, 5).
print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!