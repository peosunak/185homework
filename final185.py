#!/usr/bin/env python3
# final185.py


# Use regex to parse the GenBank file
# Store codon usage frequencey as dictionaries
# Compare individual frequencies to the whole genome frequency: 
# Use K-L or Manhattan distance for comparisons

# we will ignore comliments


import mcb185 as mcb
import argparse
import sys

parser = argparse.ArgumentParser(description='Horizontal Gene Transfer Finder.')

#reading in the file
parser.add_argument('--fasta', required=True, type=str,
	metavar='<str>', help='required FASTA File')
#argument for codon length
parser.add_argument('--thresh', required=True, type=float,
	metavar='<float>', help='required Manhatten distance')
# allow 'arg' to be used to call the argument
arg = parser.parse_args()
genome = arg.fasta
thresh = arg.thresh

seq = ''
afterorigin = False
aftergene = False
genecoords = {}

# here we are extracting the gene coordinates from genbank file
with open(genome) as fp:
	for line in fp.readlines():
		line = line.rstrip()

		if ' gene ' in line:
			if 'complement' in line: continue
			#print(line)
			lnsplit = line.split()	# find the gene coords and rid of words
			name = lnsplit[1]
			coords = name.split("..") 	# gets rid of '..' between coords
			beg = int(coords[0])-1
			end = int(coords[1])
			assert(name not in genecoords)	# makes sure we are only adding new things
			genecoords[name] = (beg, end)
		if "ORIGIN" in line: afterorigin = True	# links to the genome sequence
		if afterorigin:
			words = line.split()
			seq += ''.join(words[1:])

# now we link the gene sequence to the coordinate values
geneseq = {}
totalcodons = {}
for k, v in genecoords.items():
	gene = seq[v[0]:v[1]]
	geneseq[k] = gene
	totalcodons = mcb.codonfreq(totalcodons, gene)
# Calculate the probabilities of each codon in comparison to the whole genome
totcodons = 0
for k, v in totalcodons.items(): totcodons += v

for k, v in totalcodons.items(): totalcodons[k] = v/totcodons

# now we want make frequencies of codons for one gene and compare the usage to the whole genome
for gc, gs in geneseq.items():
	indfreq = {}		# frequency of individual codons in individual genes
	indfreq = mcb.codonfreq(indfreq, gs)
	indtot = 0
	for ic, icnt in indfreq.items(): indtot += icnt
	for ic, icnt in indfreq.items(): indfreq[ic] = icnt/indtot
	distance = mcb.manhat(totalcodons, indfreq)
	if distance > thresh:
		print(gc)


# worked with Krikor

