# Here in print formatter second last line "But it didn't sing." its output will be in double quoatation becuase
# it carries apostauphe in word "didn't".. and rest all stings will be single quoatation because they don't carry
# any word who has apostauphe.

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)