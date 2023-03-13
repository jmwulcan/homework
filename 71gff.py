# 71gff.py

# Write a program that converts genes in gff into JSON
# Use the minaturized version of the C. elegans genome (included) this time
# Organize the genes onto chromosomes
# Print the number of genes on each chromosome to stderr
# Your code should mimic the output below

# Hint: your outer data structure is a dictionary

# Note: gene names are stored differently here than the last file

import sys
import gzip
import re
import json

fp = gzip.open(sys.argv[1], 'rt')

cs = {}
genes = []
chromcount = {}
p='(\w+)(\s+\w+\s+\w+\s+)(\d+)(\s+)(\d+)(\s+.\s+)(.)(.+;sequence_name=)(.+)(;bio)'

for line in fp:
	
	match = re.search(p, line)
	if match:
		geneinfo = {}
		chromosome = match.group(1)
		geneinfo['gene'] = match.group(9)
		geneinfo['beg'] = match.group(3)
		geneinfo['end'] = match.group(5)
		geneinfo['strand'] = match.group(7)
		genes.append(geneinfo)
		if chromosome not in cs: 
			cs[chromosome]= genes
			chromcount[chromosome] = 0
		chromcount[chromosome]+= 1
			
for key, val in chromcount.items(): print(key, val, file = sys.stderr )
		
print(json.dumps(cs, indent=4))


fp.close()


"""
python3 71gff.py elegans
I 37
II 57
III 37
IV 41
MtDNA 2
V 41
X 45
{
    "I": [
        {
            "gene": "Y74C9A.6",
            "beg": 3747,
            "end": 3909,
            "strand": "-"
        },
        {
            "gene": "Y74C9A.3",
            "beg": 4116,
            "end": 10230,
            "strand": "-"
        },
...
"""
