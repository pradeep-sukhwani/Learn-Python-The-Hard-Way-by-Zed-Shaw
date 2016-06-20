# Here I'm assigning a variable x equal to the string with character (%) inside the string to put 
# formatted variable inside the strings. 
x = "There are %d types of people." % 10

# Here I'm assigning a  variable binary equal to the string.
binary = "binary"

# Here I'm assigning a variable do_not equal to a string.
do_not = "don't"

# Here I'm assigning a variable y equal to the string with character (%) inside the string to use 
# shortkey which we have assigned earlier.
y = "Those who know %s and those who %s." % (binary, do_not)

# Here I'm printing x and y.
print x
print y

# Here I'm printing a string with a character (%) inside the string and r carries a raw data of a
# variable x
print "I said: %r." % x

# Here I'm printing a string with a character (%) and has another string inside the string and r 
# carries a raw data of a variable y
print "I also said: '%s'." %y

# Here I'm assigning a variable equal to boolean character False.
hilarious = False

# Here I'm assigning a variable equal to the string with a character (%), here r carries the raw data
# of a variable 'halarious'.
joke_evaluation = "Isn't that joke so funny?! %r"

# Here I'm printing two variables.
print joke_evaluation % hilarious

# Here I'm assigning two variables equal to the string.
w = "This is the left side of..."
e = "a string with a right side."

# Here I'm printing two variables and joining them with a '+' sign
print w + e