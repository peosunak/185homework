#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Need to track 'dna' and make it so whenever it encounters a letter it prints
# the 


dna = 'ACTGAAAAAAAAAAA'
rdna = ''

for i in range(len(dna)-1, -1, -1):			#start at the -1 position, stop before -1, and itterate by -1
	if   dna[i] == 'A': rdna += 'T'				#here we are 'building' rdna
	elif dna[i] == 'T': rdna += 'A'
	elif dna[i] == 'G': rdna += 'C'
	else: rdna += 'G'
print(rdna)

# worked on this with Krikor

"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
