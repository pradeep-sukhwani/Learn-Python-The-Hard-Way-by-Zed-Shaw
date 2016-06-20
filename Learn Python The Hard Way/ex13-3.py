# combine argv with raw_input function

from sys import argv

script, gates, zuck, steve = argv

print "This script is called:", script
print "Your gates variable is:", gates
print "Your zuck variable is:", zuck
print "Your steve variable is:", steve
fourth = raw_input("What is your fourth variable? ")