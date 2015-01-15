# Adam Jaffe
# amj2158
# February 3, 2013
# file: tipcalculator.py

# This program will compute a tip by first asking how much the bill was,
# then subtracting the tax, then computing 20% of the untaxed total and rounding
# to the hundredths place (representing cents).

import math

total = input("How much is the bill total?")
untaxed=.91125*total

# The pretip is exactly 20% of the untaxed total.

pretip=.2*untaxed

# The integertip is the amount of whole dollars in the pretip
# ie for a pretip of 35.6789, the integertip is 35.00.

integertip = math.floor(pretip)

# tipcents represents the number of cents on the proper tip.

tipcents = (math.floor(round(100*(pretip-integertip))))/100
tip = integertip + tipcents

print "You should tip", tip, "dollars for a total of", tip+total, "dollars."

