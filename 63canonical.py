# 63canonical.py

# You probably learned that ATG is the only start codon, but is it?
# Write a program that reports the start codons from the E. coli genome
# Your program must:
#    1. read GCF_000005845.2_ASM584v2_genomic.gbff.gz at the only input
#    2. use a regex to find CDS coordinates
#    3. count how many different start codons there are

# Note: the sequence is at the end of the file
# Note: genes on the negative strand are marked complement(a..b)

# Hint: you can read a file twice, first to get the DNA, then the CDS
# Hint: check your CDS by examining the source protein

import sys
import gzip
import re
import mcb185

fp = gzip.open(sys.argv[1], 'rt')

# Make the whole file into a string
all = ''
for line in fp:
	all += line

# Find section in file with DNA, sections and save sequence only to 'seq'
pat1 = 'ORIGIN'
seq = ''

for match in re.finditer(pat1, all): seqstart = match.start()- 1
section = all[seqstart:]
#print (section[0:20])
pat2 = '[a-z]'
for match in re.finditer(pat2, section): seq += match.group()
seq = seq.upper()
#print(seq[0:200])

# Find cds coordinates for positive strands
posbegin = []
posend = []

pospat = '(CDS\s+)(\d+)(\.\.)(\d+)'

for match in re.finditer(pospat, all): 
	posbegin.append(int(match.group(2)))
	posend.append(int(match.group(4)))
#print(posend)


# Find CDS coordinates for negative strand
negbegin = []
negend = []

negpat = '(CDS\s+complement\()(\d+)(\.\.)(\d+)'
for match in re.finditer(negpat, all):
	negbegin.append(int(match.group(2)))
	negend.append(int(match.group(4)))
#print(negend)

#print(seq[1:10], posbegin[0], posend[0], negbegin[0], negend[0])

# Test that proteins translate correctly
#test = seq[posbegin[0]-1:posend[0]]
#testprot = mcb185.translate(test)
#print(testprot)
#test2 = seq[negbegin[0]-1: negend[0]]
#test2prot = mcb185.translate(test2, strand = '-')
#print(test2prot)

startcodons = {}
for bc in posbegin:
	startcodon = seq[bc-1:bc+2]
	if startcodon not in startcodons: startcodons[startcodon] = 0
	startcodons[startcodon] += 1

for bcneg in negend:
	startcodonneg = seq[bcneg-3:bcneg]
	compl = ''
	for nt in startcodonneg[::-1]:
		if nt == 'A': compl += 'T'
		elif nt == 'T': compl += 'A'
		elif nt == 'G': compl += 'C'
		elif nt == 'C': compl += 'G'
		else: compl += 'X'
	if compl not in startcodons: startcodons[compl] = 0
	startcodons[compl] += 1

for key, val in startcodons.items(): print(key, val)
fp.close()
"""
python3 63canonical.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gbff.gz
ATG 3883
GTG 338
TTG 80
ATT 5
AGT 1
AAA 1
AGC 1
TTC 1
TAA 1
CGT 1
CTG 2
GAC 1
"""
