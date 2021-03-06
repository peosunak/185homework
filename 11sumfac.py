#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5
sum = 0
fac = 1

for i in range(1, (n+1)):			# starting at position 1, going though 5
	sum += i						# every time the loop prints an outcome, 'X' is redefined
	fac *= i						
print(i, sum, fac)

# no indent on the print fxn only returns the final outcome
# x and y can be thought of "storage" where they take the previous value and use that as the new variable
# we want to print n, sum of 1...n, and n! on the same line print  => print(x,y,z)


# worked on this with Krikor, Maijken and Jeremy

"""
python3 11sumfac.py
5 15 120
"""
