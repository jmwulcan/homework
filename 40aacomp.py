# 40aacomp.py

# Make a program that reports the amino acid composition in a file of proteins

# Note: you are not allowed to import any libraries except gzip and sys

# Hint: gzip.open(sys.argv[1], 'rt')

# Variation: use 20 named variables
# Variation: use a list

import gzip
import sys

fp = gzip.open(sys.argv[1], 'rt')

def read_fasta(filename):
	seqs = []
	while True:
		line = fp.readline()
		if line == '': break
		line = line.rstrip()
		if line.startswith('>'): continue
		else:  seqs.append(line)
	return seqs

def counting(protein):
	A = 0
	C = 0
	D = 0
	E = 0
	F = 0
	G = 0
	H = 0
	I = 0
	K = 0
	L = 0
	M = 0
	N = 0
	P = 0
	Q = 0
	R = 0
	S = 0
	T = 0
	V = 0
	W = 0
	Y = 0
	for seq in protein:
		A += seq.count('A')
		C += seq.count('C')
		D += seq.count('D')
		E += seq.count('E')
		F += seq.count('F')
		G += seq.count('G')
		H += seq.count('H')
		I += seq.count('I')
		K += seq.count('K')
		L += seq.count('L')
		M += seq.count('M')
		N += seq.count('N')
		P += seq.count('P')
		Q += seq.count('Q')
		R += seq.count('R')
		S += seq.count('S')
		T += seq.count('T')
		V += seq.count('V')
		W += seq.count('W')
		Y += seq.count('Y')

	return A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y

seqs = read_fasta(fp)
#print(seqs)

A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y = counting(seqs)

#Generate total length of all proteins in seqs
seqs_length = 0
for seq in seqs:
	seqs_length += len(seq)

print('A', A, f'{A/seqs_length:.4F}')
print('C', C, f'{C/seqs_length:.4F}')
print('D', D, f'{D/seqs_length:.4F}')
print('E', E, f'{E/seqs_length:.4F}')
print('F', F, f'{F/seqs_length:.4F}')
print('G', G, f'{G/seqs_length:.4F}')
print('H', H, f'{H/seqs_length:.4F}')
print('I', I, f'{I/seqs_length:.4F}')
print('K', K, f'{K/seqs_length:.4F}')
print('L', L, f'{L/seqs_length:.4F}')
print('M', M, f'{M/seqs_length:.4F}')
print('N', N, f'{N/seqs_length:.4F}')
print('P', P, f'{P/seqs_length:.4F}')
print('Q', Q, f'{Q/seqs_length:.4F}')
print('R', R, f'{R/seqs_length:.4F}')
print('S', S, f'{S/seqs_length:.4F}')
print('T', T, f'{T/seqs_length:.4F}')
print('V', V, f'{V/seqs_length:.4F}')
print('W', W, f'{W/seqs_length:.4F}')
print('Y', Y, f'{Y/seqs_length:.4F}')

fp.close()
"""
python3 40aacomp.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
A 126893 0.0954
C 15468 0.0116
D 68213 0.0513
E 76890 0.0578
F 51796 0.0389
G 97830 0.0736
H 30144 0.0227
I 79950 0.0601
K 58574 0.0440
L 142379 0.1071
M 37657 0.0283
N 51896 0.0390
P 59034 0.0444
Q 59178 0.0445
R 73620 0.0554
S 76865 0.0578
T 71428 0.0537
V 94237 0.0709
W 20297 0.0153
Y 37628 0.0283
"""
