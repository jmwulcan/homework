# 61kmers.py

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

# Hint: use argparse
# Hint: use mcb185.read_fasta()

import argparse
import mcb185

parser = argparse.ArgumentParser(description = 'reports kmer counts from fasta')
parser.add_argument('file', type=str, metavar='<path>', help='fasta file')
parser.add_argument('-k', required=True, type=int, metavar='<int>', 
	help='required integer argument')
arg = parser.parse_args()


for defline, seq in mcb185.read_fasta(arg.file):
	kmers = {}
	for pos in range(0, len(seq)-1):
		kmer = seq[pos:pos+2]
		if kmer not in kmers: kmers[kmer] = 0
		kmers[kmer] += 1
	for key, val in sorted(kmers.items()): print(key, val)
	
"""
python3 60kmers.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 2
AA 338006
AC 256773
AG 238013
AT 309950
CA 325327
CC 271821
CG 346793
CT 236149
GA 267384
GC 384102
GG 270252
GT 255699
TA 212024
TC 267395
TG 322379
TT 339584
"""
