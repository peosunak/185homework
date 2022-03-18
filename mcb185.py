# mcb185.py

import sys
import gzip
import math

def read_fasta(filename):
	name = None
	seqs = []

	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()




def hcalc(prob):
	h = 0
	for p in prob:
		h += -p*math.log2(p)
	return h


def ntprobs(window):
	a = 0
	t = 0
	c = 0
	g = 0
	prob =[]
	for p in range(len(window)):
		if window[p] == 'A':
			a += 1
		if window[p] == 'T':
			t += 1
		if window[p] == 'C':
			c += 1
		if window[p] == 'G':
			g += 1
		A = a/len(window)
		T = t/len(window)
		C = c/len(window)
		G = g/len(window)
	if A > 0: prob.append(A)
	if T > 0: prob.append(T)
	if C > 0: prob.append(C)
	if G > 0: prob.append(G)
	return prob


def codonfreq(codons, sequence):
	total = 0
	for i in range(0, len(sequence)-3+1, 3):
		codon = sequence[i:i+3]
		if codon not in codons: codons[codon] = 0
		codons[codon] += 1
		total += 1
	return codons


def manhat(totdict, inddict):
	dis = 0 
	for k in totdict.keys():
		if k not in inddict: 
			dis += totdict[k]
		else:
			dis += abs(totdict[k]-inddict[k])
	return dis


# def other functions...




