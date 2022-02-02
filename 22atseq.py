#!/usr/bin/env python3

dna = ''
fnt = 0
import random
#random.seed(1) # comment-out this line to change sequence each time
for i in range(30):
	if random.random() > 0.6 :		#default value () =1
		if random.random() > 0.5:
			dna += 'G'
		else:
			dna += 'C'
	else:
		if random.random() > 0.5:
			dna += 'A'
			fnt += 1
		else:
			dna += 'T'
			fnt += 1
print(len(dna), fnt/len(dna), dna)


# create a variable fo DNA
# every time the loop occurs, I need ot add an AT or GC

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
