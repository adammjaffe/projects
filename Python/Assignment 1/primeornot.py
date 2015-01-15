# Adam Jaffe
# amj2158
# February 4, 2013
# file: primeornot.py

# This program will ask the user for an integer and tell the user if the integer
# is prime or not by checking whether or not the integer is divisible by the
# whole numbers before it. It is not limited to integers less than or equal
# to 1 million.

import math

# The first part is to ensure that the supplied integer is actually an integer
# that is positive and not equal to one. If those criteria are not met, the
# algorithm shuts down. If x=1, the integer is prime; if x=2, the integer is
# composite. If x=3, the algorithm shuts down.

integer = input("Pick an integer, any integer!!")

x=1

if integer==1:
    print "1 isn't prime, dummy!"
    x=3
if integer==0:
    print "Now how could 0 be a prime number?"
    x=3
if isinstance(integer, float):
    print "I said an integer!"
    x=3
if integer<0:
    print "Negatives can't be prime, dummy!"
    x=3
    
# I am dividing by i. If i is a factor of the integer, the integer must be
# composite. If one value of i does not work, I try again with i+1, and so
# forth.

i=2.0

# i must be a number between 2 and the square root of the integer. This is
# because at least one of the prime factors of any number must be less than
# or equal to its square root. Once x=2 (the number is proven to be not prime),
# the loop stops.

while(x<2 and i <= math.sqrt(integer)):

    # This block tests whether or not i is a factor of the integer. If it is,
    # argument will have no remainder (decimal), so determinant will equal zero.
    # If i is not a factor of the integer, argument will have a decimal, and
    # determinant must be greater than zero.

    argument=(integer/i)
    argumentinteger = math.floor(argument)
    argumentdecimal = argument - argumentinteger
    determinant = 10000*argumentdecimal

    if determinant==0:
        x=2

    i=i+1

if x==1:
    print "Yes,", integer, "is a prime number."
if x==2:
    print "No,", integer, "is not a prime number."
