def python(main, step):
	i = 0
	numbers = []
	while i < main:
		print "At the top i is %d" % i
		numbers.append(i)
		i += step
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers:"		
	for num in numbers:
		print num,
		
python(10, 2)