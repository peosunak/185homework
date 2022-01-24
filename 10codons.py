#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'
k = 3

for i in range(0,len(dna),k):	# start at position 0, loop consists of the length of 'dna', loop in steps of 'k'
	print(dna[i:i+k])			# print 'dna' starting at begining of range, which is i=0, and stopping before k

# indent the print fxn to return everything that happens before the final output

"""
python3 10codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
