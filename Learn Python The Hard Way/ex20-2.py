from sys import argv

script, input_file = argv

# defined function print_all which has a argument f (but here f is a file)
# here we print f which is argument and a .read method which reads
# the file.

def print_all(f):
    print f.read()

# Here seek method is used which means it will start from 0 (zero)
# i.e. where the file starts from
def rewind(f):
    f.seek(0)

# defined a function name print_a_line which has two
# arguments that is line_count (no. of lines)
# and same f argument (but here f is a file) from above.
def print_a_line(line_count, f):
    print line_count, f.readline()

# now here variable is declared to open i.e. a method 
# a file (input_file)
current_file = open(input_file)

# here we print out all the contents which a file carries.
# by calling a function and a varible which opens the file.
print "First let's print the whole file:\n"

print_all(current_file)

# here now we go back lets say rewind.
# in rewind function we use seek function which goes top
# of the file.
# the seek() function is dealing in bytes, not lines. The 
# code seek(0) moves the file to the 0 byte (first byte) in the file.
# again by calling a function rewind with a variable
# current_file which opens a file.
print "Now let's rewind, kind of like a tape."

rewind(current_file)

# here we print only 1st 3 lines of a file.
# here declared a variable current_line which is equal to 1
# here below the current_line variable we call the function print_a_line
# which carries line_count as a number of line and f as a file name
# here variable current_line is a number of line.
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)