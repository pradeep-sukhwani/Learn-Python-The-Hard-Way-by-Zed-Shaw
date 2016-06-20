def addition(p, s):
	print "Addition of %d and %d: " %(p, s)
	return p + s

def subtraction(p, s):
	print "Subtraction of %d and %d: " %(p, s)
	return p - s

def multiplication(p, s):
	print "Multiplication of %d and %d: " %(p, s)
	return p * s

def division(p, s):
	print "Division of %d and %d: " %(p, s)
	return p / s

print "Calling the Function:"

add = addition(500, 200)
sub = subtraction(100, 50)
mul = multiplication(40, 50)
div = division(100, 2)

print "Addition: %d, Subtraction: %d, Multiplication: %d, Division: %d" % (add, sub, mul, div)

print """
------------------------
------------------------
"""

print "Here is a puzzle:"

puzzle = addition(add, division(div, subtraction(sub, multiplication(mul, 2))))

print puzzle