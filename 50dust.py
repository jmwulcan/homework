#!/usr/bin/env python3

# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. the entropy of each window is centered (N's in the middle of windows)
# 2. has option and default value for window size (done)
# 3. has option and default value for entropy threshold (done)
# 4. has a switch for N-based or lowercase (soft) masking
# 5. works with uppercase or lowercase input files
# 6. works as an executable (done)

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description = 'Entropy filtering on fasta')
parser.add_argument('file', type=str, metavar='<path>', help='fasta file')
parser.add_argument('-w', required=False, type=int, default=11,
	metavar='<int>', help='required integer argument [%(default)i]')
parser.add_argument('-t', required=False, type=float, 
	default = 1.4, metavar='<float>', 
	help='required float argument [%(default).3f]')
parser.add_argument('--lower', action = 'store_true', 
	help = 'lower-based masking')
arg = parser.parse_args()

#print(arg.s, arg.w, arg.t)

def entropy_filter(seq, w):
	A = 0
	T = 0
	G = 0
	C = 0
	for nt in seq:
		if nt == 'A':
			A += 1
		elif nt == 'T':
			T += 1
		elif nt == 'G':
			G += 1
		elif nt == 'C':
			C += 1
	
	pA = A / w
	pT = T / w
	pG = G/ w
	pC = C / w
	
	pNTs = [pA, pT, pG, pC]
	
	H = 0
	
	for pNT in pNTs:
		if pNT != 0:
			H += - (pNT * math.log2(pNT))
	
	return H


#centerw = arg.w // 2


for defline, seq in mcb185.read_fasta(arg.file):
	seq = seq.upper()
	seq2 = list(seq)
	for i in range(len(seq) - arg.w + 1):
		wseq = seq[i:i+arg.w]
		H = entropy_filter(wseq, arg.w)
		if H < arg.t:
			for j in range(arg.w):
				if arg.lower: seq2[i+j] = seq2[i+j].lower()
				else: seq2[i+j] = 'N'

	seq2 = ''.join(seq2)
	print('>', end='')
	print(defline)
	for pos in range(0, len(seq2), 60):
		print(seq2[pos: pos+60])


"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTcATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTaaaaaaaGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAattaaaattttATTGACTTAGG
TCACTAAATacTTTAACCAATATAGGCATAGCGCACAGACAGAtAaaaaTTACAGAGTAC
ACAacATCCATGAAACGCATTAGCACCACCATTACCAccaccatCACCATTACCACAGGT
AACGGTGCgGGCTGACGCGTACAGGAAACacagaaaaAAGCCCGCACCTGACAGTGCGGG
CTttttttTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AGGCAGggGCaGGTGGCCACCGTCcTCtctgcccCcgcCAAAatcaccaacCACCTGGTG
GCGATGATTGaAAAAacCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA

Timings
win alg1 alg2
11  28.7 25.8
25  30.4 26.1
100 33.2 26.1
200 37.4 25.9
"""
