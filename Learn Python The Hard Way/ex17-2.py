# make this code shorter than the previous one

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line, how?
in_file = open(from_file).read()

print """The input file is %d bytes long
Does the ouput file exist? %r
Ready, hit RETURN to continue, CTRL-C to abort.""" %(len(in_file), exists(to_file))
raw_input()

out_file = open(to_file, 'w').write(in_file)
print "Alright, all done."