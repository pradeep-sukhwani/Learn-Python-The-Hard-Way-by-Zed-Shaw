animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

def animal(index):
    if index == 1:
        number = "1st"
    elif index == 2:
        number = "2nd"
    elif index == 3:
        number = "3rd"
    else:
        number = "%d %s" % (index, "th")
    print "The %s animal is at %d and is a %s" % (number, index-1, animals[index-1])
    print "The animal at %d is the %s animal and is a %s" % (index-1, number, animals[index-1])

for i in range(1, 7):
    animal(i)