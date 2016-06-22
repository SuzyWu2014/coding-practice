# -*- coding: utf-8 -*-
print "Let's talk about %s." % "my_name"
print "He's got %s eyes and %s hair." % ("my_eyes", "my_hair")
print "If I add %d, %d, and %d I get %d." % (
    1, 2, 3, 1 + 2 + 3)

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
