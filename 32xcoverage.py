#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

genome = int(sys.argv[1])
readnum = int(sys.argv[2])
readlen = int(sys.argv[3])
cov = []

for i in range(genome):
	cov.append(0)

for i in range(readnum):
	start = random.randint(0, genome - readlen)
	for j in range(readlen):
		cov[start + j] += 1

print(min(cov[readlen:-readlen]), max(cov[readlen:-readlen]), 
sum(cov[readlen:-readlen])/(genome - 2*readlen))

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
