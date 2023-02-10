# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below


import sys
import random

genome_size = int(sys.argv[1])
read_number = int(sys.argv[2])
read_length = int(sys.argv[3])

#Creates a list of covered positions in genome read, 1 occasion per read
covered = []
for read in range (0, read_number):
	start = random.randint(0, genome_size - read_length)
	for pos in range (start, start + read_length):
		covered.append(pos)
		
# Creates a list of how many time each position is covered
pos_coverage = []
for pos in range(0, genome_size): 
	pos_covered = covered.count(pos) 
	pos_coverage.append(pos_covered)
	
# excludes ends (undersampled)
pos_coverage_no_ends = pos_coverage[read_length:len(pos_coverage) - read_length]

#Prints results
print(min(pos_coverage_no_ends), end = ' ')
print(max(pos_coverage_no_ends), end = ' ')
print(sum(pos_coverage_no_ends)/len(pos_coverage_no_ends))



"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
