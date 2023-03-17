#!/usr/bin/env python3

# 80fastastats.py

# Write a program that reads in a FASTA file and reports the following info:
#  1. Number of sequences
#  2. Total length
#  3. Shortest sequence - name and length
#  4. Longest sequence - name and length
#  5. Median sequence length
#  6. N50 length
#  7. Composition of each letter in the sequence - name and composition
#  8. Composition of each letter in the total

import argparse
import mcb185

parser = argparse.ArgumentParser(description = 'Stats on fasta')
parser.add_argument('file', type =str, metavar='<path>', help='fasta file')
arg = parser.parse_args()

# function to calculate median

def calculate_median(l):
	l.sort()
	n = len(l)
	m = len(l)//2
	if n%2 != 0: 
		median = l[m]
	else: 
		median = (l[m] + l[m-1]) / 2
	return median

# function to calculate N50

def calculate_N50(l):
	l.sort()
	halftot = sum(l)/2
	N50_cands = [] #candidates for N50 
	tsum = 0 # temporary sum
	for x in l[::-1]:
		tsum += x
		if tsum >= halftot: N50_cands.append(x)
	N50 = max(N50_cands)
	return N50

# Alternative function to calculate N50 (slower), not in use

def calculate_N50_slow(l):
	l2 =[]
	l.sort()
	for x in l:
		ys = [x] * x
		for y in ys:
			l2.append(y)
	N50 = calculate_median(l2)
	return N50			

# Iterate through fasta_file and extract stuff

sls = {} #initiate dictionary for sequence name: sequence length
seqlens = [] #initiate list for sequence lengths
ntcountseqs = {} #initiate dictionary for name: dictionary of nt count
ntcounttotal = {}# initiate dictionary for nt: counts

for defline, seq in mcb185.read_fasta(arg.file):
	name = defline.split()[0]
	sl = len(seq) #length of each seq
	seqlens.append(sl) #add to list of all lengths of seqs in file
	sls[name]= sl #add to dictionary of seq name: seq lengths
	ntcountseq = {}	#initiate dictionary of nt: counts for each seq
	for nt in seq: 
		if nt not in ntcountseq: ntcountseq[nt] = 0
		ntcountseq[nt] += 1
		if nt not in ntcounttotal: ntcounttotal[nt] = 0
		ntcounttotal[nt] += 1
	ntcountseqs[name] = ntcountseq # add dict of nt counts in seq to dict of dicts

# Calculate number, total length

n = len(seqlens) #number of sequences
totl = sum(seqlens) #total length
shortest = min(sls.items(), key=lambda x:x[1]) #shortest seq
longest = max(sls.items(), key=lambda x:x[1]) #longest seq
median = calculate_median(seqlens) #median seq length
N50 = calculate_N50(seqlens) #N50 length

# Calculate nt composition for each seq

ntcompseqs = {} #Initiate dictionary for sequence name: dictionary of nt comp

for name, li in ntcountseqs.items(): 
	ntcompseq = {} #initiate dictionary for nt and nt composition
	for nt, c in li.items():
		l = sls[name]
		comp = c/l
		if nt not in ntcompseq: ntcompseq[nt] = comp
		#print(key, nt, c, l, comp)
	#print(name, ntcompseq)
	if name not in ntcompseqs: ntcompseqs[name] = ntcompseq



# Calculate nt composition for total file

ntcomptotal = {} # initiate dict of nt: nt composition in all seqs

for nt, c in ntcounttotal.items():
	comp = c / totl
	if nt not in ntcomptotal: ntcomptotal[nt] = comp

#Generate output

print(f'The number of sequences in the file is {n}')
print(f'The total length of all sequences in the file is {totl} nt:s')
print(f'The shortest sequence is {shortest[0]} ({shortest[1]} nt:s)')
print(f'The longest sequence is {longest[0]} ({longest[1]} nt:s)')
print(f'The median sequence length in the file is: {median} nt:s')
print(f'The N50 length for the file is: {N50} nt:s')
print('The nt composition of all sequences in the file is:')
for nt, comp in ntcomptotal.items():
	print(f' {nt}: {comp:.4F}')
for name, li in ntcompseqs.items():
	print(f'The nt composition of: {name} is:')
	for nt, comp in li.items():
		 print(f' {nt}: {comp:.4F}')



