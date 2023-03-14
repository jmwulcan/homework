#!/usr/bin/env python3

# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

import sys
import mcb185
import math

#function for entropy filtering
def entropy_filter(seq, w):

	A = 0
	T = 0
	G = 0
	C = 0
	
	for nt in seq:
		if nt == 'A': A += 1
		if nt == 'T': T += 1
		if nt == 'G': G += 1
		if nt == 'C': C += 1
	
	pA = A / w
	pT = T / w
	pG = G / w
	pC = C / w
	
	pNTs = [pA, pT, pG, pC]
	
	H = 0
	for pNT in pNTs:
		if pNT !=0:
			H += -(pNT * math.log2(pNT))
	
	return H

file = sys.argv[1]
w = int(sys.argv[2])
t = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(file):
	newseq = ''
	for i in range (len(seq)-w+1):
		wseq = seq[i: i+w]
		H = entropy_filter(wseq, w)
		if H < t: newseq += 'N'
		else: newseq += wseq[0]
	print('>', end='')
	print(defline)
	for pos in range(0, len(newseq), 60):
		print(newseq[pos: pos+60])

"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
