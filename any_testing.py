a = ['a', 'b', 'c']
str = "a123bc"

if all(x in str for x in a):
    print "yes"
else:
    print "no"