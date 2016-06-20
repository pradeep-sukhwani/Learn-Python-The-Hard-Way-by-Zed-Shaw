from sys import argv

script, user_name, learning = argv
prompt = "User: "

print "Hi %s, I'm the %s script and learning %s." % (user_name, script, learning)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "What are doing right now?"
learning = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. 
And you are %r. Nice.
""" % (likes, lives, computer, learning)