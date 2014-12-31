__author__ = 'steve1281'

"""
This file contains stuff that the book would ask you to type in at the command line.
(this allows me to record those steps in the repository)

"""

#errata - www.wrox.com/techsupport.shtml
#downloads - www.wrox.com/go/pythonprojects

aString = 'I love spam'
anotherString = 'I love spam'
anInt = 6
intAlias = anInt
print(aString == anotherString)
print(aString is anotherString)
anInt == intAlias
print(anInt is intAlias)
anInt = anInt + 1
print(intAlias)
print(anInt is intAlias)
"""
True
True
True
6
False
"""

#integer and float
print(int(5.0))
print(int('123'))
print(int('AB34',16))
"""
5
123
43828
"""

# floats cannot be converted between bases.
print(float('1.4'))
1,4

#booleans
# True   False
print(int(True))
print(int(False))
print(5 == True)
print(0 == False)
"""
1
0
False
True
"""

# the None Type (basically a null or a Nothing)
# I am not sure how to use this. The example tosses an exception
# also, the book says None is considered to have a boolean value of False
# yet:
None = False
# False
None = True
# True







