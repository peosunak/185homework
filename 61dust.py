#!/usr/bin/env python3
# 61dust.py

import argparse
import mcb185 as mcb
import sys
# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

parser = argparse.ArgumentParser(description='Masking low entropy seqs')
# required arguments
parser.add_argument('--fasta', required=True, type=str,
	metavar='<str>', help='required FASTA File')
parser.add_argument('--wins', required=True, type=int,
	metavar='<int>', help='required window size')
parser.add_argument('--ethresh', required=True, type=float,
	metavar='<float>', help='required entropy threshold')
# switches
parser.add_argument('--lowercase', action='store_true',
	help='lowercase or N based masking, N-based default')
# finalization
arg = parser.parse_args()


for name, seq in mcb.read_fasta(arg.fasta):
	seq = seq.upper()

	# create masked sequence
	output = ''
	for i in range(0, len(seq)-arg.wins+1, 1):
		prob    = mcb.ntprobs(seq[i:i+arg.wins])
		entropy = mcb.hcalc(prob)
		if entropy > arg.ethresh:
			output += seq[i]
		else:
			if arg.lowercase:
				output += seq[i].lower()
			else:
				output += 'n'
	output += seq[-arg.wins+1:]

	# output fasta file
	print(f'>{name}')
	for i in range(0, len(output), 60):
		print(output[i:i+60])

# worked on this with Krikor


