# Print statement is used to print the following string.
# Here in 2ns statement first we have a single escapes character, then we have
# we have a escape character than new line escape character and horizontal tab.
print "Let's pratice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# Here triple quotation is used for extended string.
# in 1st line we have a horizontal tab, 3rd line new line,
# 6th line a new line and 2 times horizontal tab.
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# Print statement is used to print the following string.
print "--------------"
print poem
print "--------------"

# Assigned a new variable 'five' which has a 
# string conversion character which will print the total of number of a variable 'five'
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# Declared a function.
# assigned new variables
# then we use return statement to return the values to its caller.
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

# Assigned a new variable 'start_point'.
# Assigned a new variable i.e. equal to a function.
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# Changed the value of the variable.
start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)