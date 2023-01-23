# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

GC = 0

for i in dna:
	if i == 'G' or i == 'C': GC += 1 #Creates variable with number of G or C in DNA

GC_cont = GC/(len(dna)) #creates variable with GC%

print(f'{GC_cont:.2f}') #prints with two decimal planes
"""
python3 24gc.py
0.42
"""
