#!/usr/bin/python
"""
---------------Multi-Line Statements-----------------------
"""
############################################################
total = item_one + \
        item_two + \
        item_three
############################################################
"""
-----------------------Variable Types-----------------------
"""
############################################################
a, b, c = 1, 2, "john"
# Numbers
long_int = 32554353L
# String
str = 'Hello World!'

print str          # Prints complete string
print str[0]       # Prints first character of the string
print str[2:5]     # Prints characters starting from 3rd to 5th
print str[2:]      # Prints string starting from 3rd character
print str * 2      # Prints string two times
print str + "TEST" # Prints concatenated string
#Result
# Hello World!
# H
# llo
# llo World!
# Hello World!Hello World!
# Hello World!TEST
# List
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 3rd 
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists

# Result
# ['abcd', 786, 2.23, 'john', 70.200000000000003]
# abcd
# [786, 2.23]
# [2.23, 'john', 70.200000000000003]
# [123, 'john', 123, 'john']
# ['abcd', 786, 2.23, 'john', 70.200000000000003, 123, 'john']

# Tuple
# A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.
# The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists. 
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print tuple           # Prints complete list
print tuple[0]        # Prints first element of the list
print tuple[1:3]      # Prints elements starting from 2nd till 3rd 
print tuple[2:]       # Prints elements starting from 3rd element
print tinytuple * 2   # Prints list two times
print tuple + tinytuple # Prints concatenated lists
#Result
# ('abcd', 786, 2.23, 'john', 70.200000000000003)
# abcd
# (786, 2.23)
# (2.23, 'john', 70.200000000000003)
# (123, 'john', 123, 'john')
# ('abcd', 786, 2.23, 'john', 70.200000000000003, 123, 'john')
# Dictionary
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values
#Result
# This is one
# This is two
# {'dept': 'sales', 'code': 6734, 'name': 'john'}
# ['dept', 'code', 'name']
# ['sales', 6734, 'john']
#Data Type Conversion
int(x [,base])			# Converts x to an integer. base specifies the base if x is a string.
long(x [,base] )		# Converts x to a long integer. base specifies the base if x is a string.
float(x)				# Converts x to a floating-point number.
complex(real [,imag])	# Creates a complex number.
str(x)					# Converts object x to a string representation.
repr(x)					# Converts object x to an expression string.
eval(str) 				# Evaluates a string and returns an object.
tuple(s)				# Converts s to a tuple.
list(s)					# Converts s to a list.
set(s)					# Converts s to a set.
dict(d)					# Creates a dictionary. d must be a sequence of (key,value) tuples.
frozenset(s)			# Converts s to a frozen set.
chr(x)					# Converts an integer to a character.
unichr(x)				# Converts an integer to a Unicode character.
ord(x)					# Converts a single character to its integer value.
hex(x)					# Converts an integer to a hexadecimal string.
oct(x)					# Converts an integer to an octal string.
############################################################
"""
-----------------------while Loop--------------------------
"""
############################################################
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"
############################################################
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"
############################################################
"""
-----------------------For Loop----------------------------
"""
############################################################

for letter in 'Python':     # First Example
   print 'Current Letter :', letter

############################################################
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print 'Current fruit :', fruit

print "Good bye!"
############################################################

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print 'Current fruit :', fruits[index]

print "Good bye!"

for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print num, 'is a prime number'
############################################################

