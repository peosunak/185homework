#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

prob = []
H = 0

for item in sys.argv[1:]:
	prob.append(float(item))

for p in prob:			# this is a summing up opperation, no need for a 'sum' var
	H += -p*math.log2(p)
print(f'{H:.3f}')


# worked on this with krikor
"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
