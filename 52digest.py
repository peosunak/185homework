#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments

"""
# good checkpoint to learn from
afterorigin = False		# sets everything in the lines to 'False', or not valid, until the condition is met
seq = ''
with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		if line.startswith("ORIGIN"):
			afterorigin = True 		# here everything on the lines has been false, now that we have arrived at "ORIGIN", lines are valid 
		if afterorigin: 		# saying if after origin is valid, which it is now
			words = line.split()	# puts each item of the line into a list
			print(words[1:])
"""
#print(seq)
afterorigin = False
seq = ''
with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		if line.startswith("ORIGIN"):
			afterorigin = True 		
		if afterorigin: 		
			words = line.split()	
			# now we want to add to our seq from our newly created list
			seq += ''.join(words[1:]) # this smushed together our list from the 1st item and on (excluding the numbers)
			# print(seq)

redig = sys.argv[2]

start = [0]
for match in re.finditer(redig, seq):	# 'refinditor' used to find a pattern multiple times in a string
	start.append(match.start())
start.append(len(seq))
# print(match)

for i in range(len(start)-1):
	x = start[i+1] - start[i]
	print(x)


"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
