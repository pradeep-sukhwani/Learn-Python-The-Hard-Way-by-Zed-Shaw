from sys import argv

script, filename = argv

text = open(filename)

print "Here is your file %r" % (filename)
print text.read()
text.close()