# define function add with 2 arguments a and b
# then printing the string with characters
# then we just return a + b.
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

# define function subract with 2 arguments a and b
# then printing the string with characters
# then we just return a - b.
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

# define function multiply with 2 arguments a and b
# then printing the string with characters
# then we just return a * b.
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

# define function divide with 2 arguments a and b
# then printing the string with characters
# then we just return a / b.
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

# printing the string.
# This is the first thing that will print because
# the print commands above in the function
# haven't been called yet.
print "Let's do some math with just functions!"

# declared variable and calling the function.
# age is calling add, height is calling subtract,
# weight is calling multiply, iq is calling divide.
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# printing the variable with string characters.
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# declared a variable what is equal to a set of function's result.
# here python observes the order of operation by doing the 
# innermost parentheses i.e.:
# first we divide iq with 2 then multiply weight with iq result
# then subtract height with weight result, then add age with subtract result.
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"