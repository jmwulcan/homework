# 27frame.py

# Write a program that prints out the position, frame, and letter of the DNA

# Variation: try coding this with a single loop and nested loops

# Note: use 0-based indexing for position and frame (biology uses 1-based)

dna = 'ATGGCCTTT'

for nt in range(len(dna)):
	print(nt, end = ' ')
	if nt % 3 == 0: print(0, end = ' ')
	if nt % 3 == 1: print(1, end = ' ')
	if nt % 3 == 2: print(2, end = ' ')
	print(dna[nt])

"""
python3 27frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
