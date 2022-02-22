#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

# we want to type '3 1 4 1 5' in the command line
# first we have to turn what we type from 'text' to a usable 'number'

box = []			# this creates a 'container' to which our command line is entered
for item in sys.argv[1:]:		# this turns our input into actual numbers
	box.append(int(item))


# Count
box.sort()				# need this to order our input, default is in ascending order
count = len(box)
print('Count:', count)


# Min & Max
Min = box[0]
Max = box[-1] # just 'len(box)' returns a value 'out of range'

print('Minimum:', '%.1f' % Min)
print('Maximum:', '%.1f' % Max)


# Mean
# For the mean, we need to add all our values together then divide
# need to create a variable that stores our addition as we itterate thought the list

sum = 0 	# variable needs to be empty when we start
for val in box:
	sum += val
mean = sum/len(box)
print('Mean:', '%.3f' % mean)


# Std. Dev
# we want the sqr rt of the (sum of values - mean)/size of population
# soooo sqrt of (sum - (sum/len(box)) / count)

sd = 0 
for val in box:
	sd += ((val-mean)**2) # 'sum' did not work here, maybe cuz it was adding them all together
print('Std. dev:', '%.3f' % (math.sqrt(sd/count)))


# Median (middle number of string)
median = None
							# odd calc
if count % 2 == 1: 
	median = box[count//2]
else:						# even calc
	hi = box[count//2]
	lo = box[count//2 -1]
	median = (hi+lo)/2
print('Median:', '%.3f' % median)

# worked on this with krikor

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
