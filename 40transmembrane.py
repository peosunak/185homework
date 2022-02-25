#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix


def kd_hydropathy(seq):
	kd = 0
	for aa in seq:
		if   aa == 'I': kd += 4.5
		elif aa == 'V': kd += 4.2
		elif aa == 'L': kd += 3.8
		elif aa == 'F': kd += 2.8
		elif aa == 'C': kd += 2.5
		elif aa == 'M': kd += 1.9
		elif aa == 'A': kd += 1.8
		elif aa == 'G': kd += -0.4
		elif aa == 'T': kd += -0.7
		elif aa == 'S': kd += -0.8
		elif aa == 'W': kd += -0.9
		elif aa == 'Y': kd += -1.3
		elif aa == 'P': kd += -1.6
		elif aa == 'H': kd += -3.2
		elif aa == 'E': kd += -3.5
		elif aa == 'Q': kd += -3.5
		elif aa == 'D': kd += -3.5
		elif aa == 'N': kd += -3.5
		elif aa == 'K': kd += -3.9
		elif aa == 'R': kd += -4.5
	return kd/(len(seq))

# signal peptide 8 long hydrophobic 2.5

def ahelix(seq, size, thold):
	for i in range(len(seq) - size+1):
		peptide = seq[i:i+size]
		if 'P' in peptide : continue
		if kd_hydropathy(peptide) >= thold:
			return True
	return False
# if ahelix('MAGPNVAARSVLSWP', 8, 1.0):
#	print('found signal peptide')


# I need to read all of the sequences in , not just lines
# can make two lists, one with names and one with sequences

seqs  = []
names = []
sequence = ''
with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		line = line.rstrip()

		if len(line) == 0: continue
		if line[0] == '>':
			if len(sequence) > 0: seqs.append(sequence)
			sequence = ''
			words = line.split()
			names.append(words[0][1:])
		else: 
			sequence += line
	seqs.append(sequence)

for name, sequence in zip(names, seqs): 
	if ahelix(sequence[0:30], 8, 2.5) and ahelix(sequence[30:], 11, 2.0):
		print(name)

# find the > sign and return the thing after it
# check each seq for hydrophobicity parameters, if both domains, give name

# worked on this with Krikor
"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
