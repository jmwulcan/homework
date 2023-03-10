# 62orfs.py

# Make a program that finds open reading frames in the E. coli genome
# Your program should read a fasta file
# There should be an optional minimum ORF size with a default value of 300 nt
# The output should be a table showing 4 columns
#     1. parent sequence identifier
#     2. begin coordinate
#     3. end coordinate
#     4. strand
#     5. first 10 amino acids of the protein

# Hint: use argparse, mcb185.read_fasta(), and mcb185.translate()
# Hint: don't use the whole genome for testing

# Note: your genes should be similar to those in the real genome




import argparse
import mcb185

parser=argparse.ArgumentParser(description='finds ORFs in fasta file')
parser.add_argument('file', type=str, metavar='<path>', help='some file')
parser.add_argument('--orf', required = False, type=int, default=300, 
	 metavar='<int>', help='optional integer argument [%(default)i]')
arg = parser.parse_args()

				
def orf (seq, size=0, rev=False):
	if rev: seq = mcb185.anti(seq)
	
	for i in range(3):
		while i <= len(seq) - 3:
			codon = seq[i:i+3]
			if codon == 'ATG':
				for j in range(i+3, len(seq)-2, 3):
					codon = seq[j:j+3]
					if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
						if j-i > size:
							if rev:
								yield len(seq)-j-2, len(seq)-i, mcb185.translate(seq[i:j+2])
							else:
								yield i+1, j+3, mcb185.translate(seq[i:j+2])
						i = j
						break
			i+=3
	
for defline, seq in mcb185.read_fasta(arg.file):
	name = defline.split()[0]
	orfs = {}
	for beg, end, pro in orf(seq, arg.orf):
		print(name, beg, end, '+', pro[:10])
	for rbeg, rend, rpro in orf(seq, arg.orf, True):
		print(name, rbeg, rend, '-', rpro[:10])

				
			

"""
python3 62orfs.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz
NC_000913.3 108 500 - MVFSIIATRW
NC_000913.3 337 2799 + MRVLKFGGTS
NC_000913.3 2801 3733 + MVKVYAPASS
NC_000913.3 3512 4162 - MSHCRSGITG
NC_000913.3 3734 5020 + MKLYNLKDHN
NC_000913.3 3811 4119 - MVTGLSPAIW
NC_000913.3 5310 5738 - MKIPPAMANW
NC_000913.3 5683 6459 - MLILISPAKT
NC_000913.3 6529 7959 - MPDFFSFINS
NC_000913.3 7366 7773 + MKTASDCQQS
"""
