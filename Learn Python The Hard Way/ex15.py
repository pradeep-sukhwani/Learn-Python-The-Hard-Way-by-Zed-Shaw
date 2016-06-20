from sys import argv

# here we have two variables i.e. script and filename, in this ex. 
# we have created two files i.e. one .py file another is .txt file 
# i.e. our filename which we use now.
script, filename = argv

# Here txt equal open(filename) this says to open a .txt file 
# which ex15_sample. open is used to open a file
txt = open(filename)

# here we print the sting before opening a file a string carries
# character %r which is a filename
print "Here's your file %r:" % filename
# here we say that read a txt file. the . (dot, period) says to do
# something and that something is read a txt file.
print txt.read()

# here we are printing the string
print "Type the filename again:"

# a variable file_again is used to raw_input to open a file.
file_again = raw_input("> ")

# txt_again is used to open file_again
txt_again = open(file_again)

# here we say that read a txt file. the . (dot, period) says to do
# something and that something is read a txt file.
print txt_again.read()
txt.close()
txt_again.close()