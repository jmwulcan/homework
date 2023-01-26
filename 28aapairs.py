# 28aapairs.py

# Print out all the unique pairwise amino acid combinations
# AC is the same as CA
# Skip AA, CC etc.
# Also print out how many combinations there are

# Hint: if you get stuck for more than 10 minutes, get help

aa = 'ACDEFGHIKLMNPQRSTVWY' #variable of all amino acids

#Creates a variable containing all unique pairwise combinations. There is
#probably a better way.

aa_pair = ''
for i in aa:
	if i != 'A': aa_pair += 'A' + i
for i in aa:
	if i != 'A' and i !='C': aa_pair += 'C' + i
for i in aa:
	if i != 'A' and i !='C' and i !='D': aa_pair += 'D' + i
for i in aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E': aa_pair += 'E' + i
for i in aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E' and i != 'F': \
	aa_pair += 'F' + i
for i in aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E' and i != 'F' and \
	i != 'G': aa_pair += 'G' + i
for i in aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E' and i != 'F' and i != 'G'\
	and i != 'H': aa_pair += 'H' + i
for i in aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E' and i != 'F' and i != 'G'\
	and i != 'H' and i != 'I': aa_pair += 'I' + i
for i in  aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E' and i != 'F' and i != 'G'\
	and i != 'H' and i != 'I' and i !='K': aa_pair += 'K' + i
for i in  aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E' and i != 'F' and i != 'G'\
	and i != 'H' and i != 'I' and i !='K' and  i != 'L': aa_pair += 'L' + i
for i in  aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E' and i != 'F' and i != 'G'\
	and i != 'H' and i != 'I' and i !='K' and  i != 'L' and i !='M' \
	: aa_pair += 'M' + i
for i in  aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E' and i != 'F' and i != 'G'\
	and i != 'H' and i != 'I' and i !='K' and  i != 'L' and i !='M' and i !='N'\
	: aa_pair += 'N' + i
for i in  aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E' and i != 'F' and i != 'G'\
	and i != 'H' and i != 'I' and i !='K' and  i != 'L' and i !='M' and i !='N'\
	and i != 'P': aa_pair += 'P' + i
for i in  aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E' and i != 'F' and i != 'G'\
	and i != 'H' and i != 'I' and i !='K' and  i != 'L' and i !='M' and i !='N'\
	and i != 'P' and i != 'Q': aa_pair += 'Q' + i
for i in  aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E' and i != 'F' and i != 'G'\
	and i != 'H' and i != 'I' and i !='K' and  i != 'L' and i !='M' and i !='N'\
	and i != 'P' and i != 'Q' and i != 'R': aa_pair += 'R' + i
for i in  aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E' and i != 'F' and i != 'G'\
	and i != 'H' and i != 'I' and i !='K' and  i != 'L' and i !='M' and i !='N'\
	and i != 'P' and i != 'Q' and i != 'R' and i != 'S': aa_pair += 'S' + i
for i in  aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E' and i != 'F' and i != 'G'\
	and i != 'H' and i != 'I' and i !='K' and  i != 'L' and i !='M' and i !='N'\
	and i != 'P' and i != 'Q' and i != 'R' and i != 'S' and i !='T':\
	 aa_pair += 'T' + i
for i in  aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E' and i != 'F' and i != 'G'\
	and i != 'H' and i != 'I' and i !='K' and  i != 'L' and i !='M' and i !='N'\
	and i != 'P' and i != 'Q' and i != 'R' and i != 'S' and i !='T' and i !='V'\
	: aa_pair += 'V' + i
for i in  aa:
	if i != 'A' and i != 'C' and i !='D' and i != 'E' and i != 'F' and i != 'G'\
	and i != 'H' and i != 'I' and i !='K' and  i != 'L' and i !='M' and i !='N'\
	and i != 'P' and i != 'Q' and i != 'R' and i != 'S' and i !='T' and i !='V'\
	and i != 'W': aa_pair += 'W' + i

# Prints the pairs in a format similar to expected output

for position in range(0, len(aa_pair) - 1, 2):
	print(aa_pair[position], end = ' ')
	print(aa_pair[position + 1])

#Calculates number of combinations and prints the number as an integer

comb = len(aa_pair)/2
comb = int(comb)
print(comb)


"""
python3 28aapairs.py
A C
A D
A E
A F
A G
A H
A I
A K
A L
A M
A N
A P
A Q
A R
A S
A T
A V
A W
A Y
C D
C E
C F
C G
C H
C I
C K
C L
C M
C N
C P
C Q
C R
C S
C T
C V
C W
C Y
D E
D F
D G
D H
D I
D K
D L
D M
D N
D P
D Q
D R
D S
D T
D V
D W
D Y
E F
E G
E H
E I
E K
E L
E M
E N
E P
E Q
E R
E S
E T
E V
E W
E Y
F G
F H
F I
F K
F L
F M
F N
F P
F Q
F R
F S
F T
F V
F W
F Y
G H
G I
G K
G L
G M
G N
G P
G Q
G R
G S
G T
G V
G W
G Y
H I
H K
H L
H M
H N
H P
H Q
H R
H S
H T
H V
H W
H Y
I K
I L
I M
I N
I P
I Q
I R
I S
I T
I V
I W
I Y
K L
K M
K N
K P
K Q
K R
K S
K T
K V
K W
K Y
L M
L N
L P
L Q
L R
L S
L T
L V
L W
L Y
M N
M P
M Q
M R
M S
M T
M V
M W
M Y
N P
N Q
N R
N S
N T
N V
N W
N Y
P Q
P R
P S
P T
P V
P W
P Y
Q R
Q S
Q T
Q V
Q W
Q Y
R S
R T
R V
R W
R Y
S T
S V
S W
S Y
T V
T W
T Y
V W
V Y
W Y
190
"""
