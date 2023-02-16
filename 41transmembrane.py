# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane

import sys
import mcb185

# function that calculated KD value for a sequence
def hydrop (subseq):

	KD = 0
	
	for aa in subseq:
		if aa == 'I':
			KD += 4.5
		elif aa == 'V':
			KD += 4.2
		elif aa == 'L':
			KD += 3.8
		elif aa == 'F':
			KD += 2.8
		elif aa == 'C':
			KD += 2.5
		elif aa == 'M':
			KD += 1.9
		elif aa == 'A':
			KD += 1.8
		elif aa == 'G':
			KD += -0.4
		elif aa == 'T':
			KD += -0.7
		elif aa == 'S':
			KD += -0.8
		elif aa == 'W':
			KD += -0.9
		elif aa == 'Y':
			KD += -1.3
		elif aa == 'P':
			KD += -1.6
		elif aa == 'H':
			KD += -3.2
		elif aa == 'E':
			KD += -3.5
		elif aa == 'Q':
			KD += -3.5
		elif aa == 'D':
			KD += -3.5
		elif aa == 'N':
			KD += - 3.5
		elif aa == 'K':
			KD += -3.9
		elif aa == 'R':
			KD = -4.5
		else: continue
	return KD

# function that calculates number of Proline (used to id alpha Helix)
def prolines (subseq):
		
	P = 0
	for aa in subseq:
		if aa == 'P':
			P += 1
		else: continue
	return P
		
	
proteome = sys.argv[1]

for name_def, seq in mcb185.read_fasta(proteome):
	
	sigpep = 0
	hreg = 0
	
	w1 = 8
	for pos in range(0, 30 - w1 + 1):
		subseq = seq[pos:pos+w1]
		KD = hydrop(subseq)
		P = prolines(subseq)
		if KD /w1 > 2.5 and P == 0:
			sigpep += 1
	
	
	w2 = 11
	for pos in range(31, len(seq) - w2 + 1):
		subseq = seq[pos:pos+w2]
		KD = hydrop(subseq)
		P = prolines(subseq)
		if KD / w2 > 2.0 and P == 0:
			hreg += 1
	
	#print(sigpep, hreg)
	if sigpep != 0 and hreg != 0:
		print(name_def)
	
"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
