#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

for i in range(len(dna)):
	print(i, i%3, dna[i])
print('end of single loop')

# for the nested loop we want to dfine each reading frame

for i in range(0, len(dna), 3):
	for n in range(3):
		print(i+n, n, dna[i+n])
print('end of nested loop')

# worked on this with Krikor

"""
python3 24frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
