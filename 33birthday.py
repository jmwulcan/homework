# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list


import sys
import random

days = int(sys.argv[1])
people = int(sys.argv[2])
iterations = 10000

outcome = 0
for i in range(iterations):
	bday_list = []
	repeats = 0
	for person in range(people):
		bday = random.randint(1, days)
		if bday in bday_list: repeats += 1
		else: bday_list.append(bday)
	if repeats > 0: it_happened = 1
	else: it_happened = 0
	outcome += it_happened
print(f'{outcome/iterations: .3f}')




"""
python3 33birthday.py 365 23
0.571
"""
