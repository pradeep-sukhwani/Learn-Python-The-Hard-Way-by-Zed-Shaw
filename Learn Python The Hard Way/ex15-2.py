
# here we are printing the string
print "Type the filename again:"

# a variable file_again is used to raw_input to open a file.
file_again = raw_input("> ")

# txt_again is used to open file_again
txt_again = open(file_again)

# here we say that read a txt file. the . (dot, period) says to do
# something and that something is read a txt file.
print txt_again.read()