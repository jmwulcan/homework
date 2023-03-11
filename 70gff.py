# 70gff.py

# Write a program that converts genes in gff into JSON
# Use the E. coli genome gff
# Your code should mimic the output below

# Make a list
# make dictionaries each containing  keys gene, beg, end and strand

import sys
import gzip
import re
import json

fp = gzip.open(sys.argv[1], 'rt')
allgenes = []

genepat = '(gene\s+)(\d+)(\s+)(\d+)(\s+.\s+)(.)(\s+.+;Name=)(.+)(;gbkey)'

for line in fp:
	geneinfo = {}
	match = re.search(genepat, line)
	if match:
		geneinfo['gene'] = match.group(8)
		geneinfo['beg'] = match.group(2)
		geneinfo['end'] = match.group(4)
		geneinfo['strand'] = match.group(6)
		print(geneinfo)
		allgenes.append(geneinfo)


print(json.dumps(allgenes, indent=4))



fp.close()
"""
python3 70gff.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gff.gz
[
    {
        "gene": "thrL",
        "beg": 190,
        "end": 255,
        "strand": "+"
    },
    {
        "gene": "thrA",
        "beg": 337,
        "end": 2799,
        "strand": "+"
    },
...
"""
