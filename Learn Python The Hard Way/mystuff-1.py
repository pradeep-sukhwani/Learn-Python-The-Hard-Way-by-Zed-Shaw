# dict style
mystuff['apples']

# module style
import mystuff
mystuff.apple()
print mystuff.tangerine

mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from module
mystuff.tangerine # same thing, it's just a variable

# class style
thing = MyStuff()
thing.apple()
print thing.tangerine