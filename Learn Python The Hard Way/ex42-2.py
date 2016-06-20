class Animal(object):
	
	def __init__(self, type, name):
	
		self.name = name
		
	def show_info(self):
		
		print "Name: " + self.name
		
class Dog(Animal):

	def __init__(self, type, name):
		
		self.type = type
		Animal.__init__(self, type, name)
	
	def show_info(self):

		print "Type of Dog: " + self.type	
		Animal.show_info(self)

class Cat(Animal):
	
	def __init__(self, type, name):
		
		self.type = type
		Animal.__init__(self, type, name)
	
	def show_info(self):

		print "Type of Cat: " + self.type	
		Animal.show_info(self)
		
class Person(object):

	def __init__(self, name, company, salary, pet):
		self.name = name
		self.company = company
		self.salary = salary
		self.pet = pet
	
	def show_info(self):
		print "Name: " + self.name
		print "Company: " + self.company
		print "Salary: " + str(self.salary)
		print "Pet's Name: " + str(self.pet)
		
class Employee(Person):

	def __init__(self, name, company, salary, pet):
		Person.__init__(self, name, company, salary, pet)
		
	def show_info(self):
		Person.show_info(self)

		
class Fish(object):

	def __init__(self, type, name):
	
		self.type = type
		self.name = name
		
	def show_info(self):
		
		print "Type of fish: " + self.type
		print "Name: " + self.name
		
ceaser = Dog("Hungarian Sheepdog", "Beast")
pitbull = Dog("Pug", "Pitbull")

shelly = Cat("Persian Cat", "Shelly")
molly = Cat("Siamese Cat", "Molly")

jacob = Fish("Jelly Fish", "Jacob")
nicolie = Fish("Gold Fish", "Nicolie")

mark = Employee("Mark Zukerburg", "Facebook", 100000, 1)
bill = Employee("Bill Gates", "Microsoft", 50000, None)
steve = Employee("Steve Jobs", "Apple", 100000, 1)
sundar = Employee("Sundar Pichai", "Google", 1000000, None)

mark.pet = "Beast"
steve.pet = "Pitbull"

print "\n"
ceaser.show_info()
print "\n"
pitbull.show_info()
print "\n"

shelly.show_info()
print "\n"
molly.show_info()
print "\n"

jacob.show_info()
print "\n"
nicolie.show_info()
print "\n"

mark.show_info()
print "\n"
bill.show_info()
print "\n"
steve.show_info()
print "\n"
sundar.show_info()
print "\n"