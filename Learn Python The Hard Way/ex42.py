## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## Dog is-a instance of object Animal
class Dog(Animal):

	def __init__(self.name):
		## Dog has-a name
		self.name = name
		
## Cat is-a instance of object Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name
		
## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
## Employee ia-a instance of object Person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee is-a Person hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary
		
## Fish is-a object
class Fish(object):
	pass

## Salmon is-a instance of object Fish
class Salmon(Fish):
	pass
	
## Halibut is-a instance of object fish
class Halibut(Fish):
	pass
	

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a cat named satan
mary.pet = satan

## frank is-a employee has-a 120000 salary
frank = Employee("Frank", 120000)

## frank has-a dog named rover
frank.pet = rover

## flipper is-a name of object fish
flipper = fish()

## crouse is-a name of Salmon
crouse = Salmon()

## harry is-a name of Halibut
harry = Halibut()