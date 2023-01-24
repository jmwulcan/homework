# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'

compl=''
for nt in dna:
	if nt == 'A': compl = compl + 'T'
	elif nt == 'T': compl = compl + 'A'
	elif nt == 'G': compl = compl + 'C'
	elif nt == 'C': compl = compl +'G' #Creates complement string

rev = compl[::-1] #creates reverse complement string

print(rev)

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
