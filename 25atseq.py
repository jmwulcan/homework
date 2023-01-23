# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

import random

random.seed(5)

rand_dna = ''
AT = 0

for nt in range (1, 31):
	nt = random.choice('AAATTTCCGG') #60% A or T in the letters to pick from
	rand_dna = str(rand_dna) + nt   #generates random sequence

for nt in rand_dna:
	if nt == 'A' or nt == 'T': AT += 1 #calculates number of nt that are A or T

AT_fraction = AT / (len(rand_dna))

print(len(rand_dna), end = ' ')
print(AT_fraction, end = ' ')
print(rand_dna)

"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
