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

#collection types
# strings, bytes, tuples, lists, dictionaries and sets
# determine the length of any collection with the len() function
a = "this is a test"
print(len(a))
#individial elements accessed via indexing
print(a[3])
# or you can slice, using a :
print(a[:3])
print(a[3:])
print(a[3:4])
print(a[::3]) # neat. from beginning to end, every third
# better example would be:
c = list(range(0,30))
print(c[0])
print(c[:5])
print(c[::5])
#

#
#  strings
#
'using single quotes'
"using double quotes"
print('''triple single quotes spanning
... multiple lines ''')

"""
+ concatenation
* multiplication
upper, lower, capitalize
center, ljust, rjust
startswith, endswith
find, index, rfind
isalpha, isdigit, isalnum,
join
split, splitlines, parition
strip, lstrip, rstrip
replace
format
"""

#
# byte array
#
# typically only used in network communicaton
s = b'Alphabet soup'
print(type(s))
c = b'A'
print(s[0] == c)
print(s[0] == c[0])
"""
<class 'bytes'>
False
True
"""

#
#  tuples
#
print(divmod(12,7))
# (1, 5)
q,r = divmod(12,7)
print(q)
# 1
print(r)
# 5

() == False
# False
() == True
# False
(1) == False
# False
(1) == True
# True

# lists
[n*n for n in range(1,11) if not n*n %2]
# [4, 16, 36, 64, 100]

#operations
#+
#*
#append
#extend
#pop
#index
#count
#insert
#remove
#reversed
#sort
c = [n*n for n in range(1,11) if not n*n %2]
print(c)
[4, 16, 36, 64, 100]
c.pop()
print(c)
[4, 16, 36, 64]


#dictionaries
c = {'aKey':'avalue',2:7, 'booleans':{False:0, True:1}}
print(c)
# {'aKey': 'avalue', 2: 7, 'booleans': {False: 0, True: 1}}
print(c['booleans'])
# {False: 0, True: 1}
print(c['booleans'][True])
# 1

# keys, values, items
# get, pop
# setdefault
# fromkeys
c = {'aKey':'avalue',2:7, 'booleans':{False:0, True:1}}
x = list(c.keys())
print(x)
# ['aKey', 2, 'booleans']
x = list(c.values())
print(x)
# ['avalue', 7, {False: 0, True: 1}]

# sets
myset = {1,2,3,4,5}
# no indexing, no slicing, no inherit order

# in
# issubset, <=, <
# issuperset, >=, >
# union, |
# intersection, &
# difference, -
# symmetric_difference, ^
# ...
# update, |=
# intersection_update, &=
# difference_update, -=
# symmetric_difference_update, ^=
# add
# remove
# discard
# pop
# clear

# examples ...



# structuring your program
# tradionally startup  module code is put in a function called main().
# it is not strically necessary however.
# the startup looks like
"""
if __name__ == "__main__":
    main()
"""

# this bootstrapping works because if
# a module is loaded from interupter __name__ is set
# if imported, it is not.













