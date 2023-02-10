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

#Creates list with position, and how many times they are covered
covered = [0] * genome_size #Empty list same size as genome

for read in range (0, read_number):
	start = random.randint(0, genome_size - read_length)
	for pos in range (start, start + read_length):
		covered[pos] += 1

#excludes ends (undersampled)
no_ends = covered[read_length:len(covered) - read_length]

#Prints results
print(min(no_ends), end = ' ')
print(max(no_ends), end = ' ')
print(sum(no_ends)/len(no_ends))



"""	
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
