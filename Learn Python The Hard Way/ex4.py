# According to python, we have to assure about variable names for an ex.: on line number 19 carpool_capacity
# is a variable but car_pool_capacity is not since we have not declined "car_pool_capacity" is variable.
# So it will show you an error about car_pool_capacity because it is not defined as variable.

# Here I'm assigning a variable cars equal to number 100.
cars = 100

# Here I'm assigning a variable space_in_a_car equal to number 4.
space_in_a_car = 4

# Here I'm assigning a variable drivers equal to number 30.
drivers = 30

# Here I'm assigning a variable passengers equal to number 90.
passengers = 90

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "These are", cars, "cars available."
print "These are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."