# Here we are defining the function i.e. cheese_and_crackers
# with def with two arguments i.e. cheese_count and boxes_of_crackers. 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheese!" %cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# This prints the string into the command line.
print "We can just give the function numbers directly:"

# Here we are defining the values of cheese and crackers.
cheese_and_crackers(20,30)

# This print the string into the command line.
print "OR, we can use variables from our scripts:"

# Here we aare declaring the variables for defining the
# the value of cheese and crackers.
amount_of_cheese = 10
amount_of_crackers = 50

# Here we are calliing the function this is variable method, here 
# we print the value of cheese and crackers by this method.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# This print the string into the command line.
print "We can even do math inside too:"

# Here we call the function and doing the math.
cheese_and_crackers(10+20, 5+6)

# This prints the string into the command line.
print "And we can combine the two, variables and math:"

# This combines the varibles with numbers and do the math.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)