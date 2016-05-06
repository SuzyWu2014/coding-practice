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

# String

# List

# Tuple

# Dictionary
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

