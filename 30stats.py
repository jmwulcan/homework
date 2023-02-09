# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

#Calculate count
nums=len(sys.argv[1:])

# Calculate mean
tot = 0
for i in sys.argv[1:]:
	tot += float(i)
mean = tot/nums

#Calculate standard deviation
sum_diff_squared = 0
for i in sys.argv[1:]:
	diff_squared = (float(i) - mean)**2
	sum_diff_squared += diff_squared
sd =	(sum_diff_squared/nums)**0.5

#Calculate median 
mid = nums // 2
vec = ''
for i in sys.argv[1:]:
	vec += i
vec_list = list(vec)
vec_list.sort()
if nums%2 != 0:
	median = float(vec_list[mid])
if nums%2 == 0:
	median_low = float(vec_list[mid])
	median_high = float(vec_list[mid + 1])
	median = (median_low + median_high) /2

#Print output
print(f'Count: {nums}')
print(f'Minimum: {float(min(sys.argv))}')
print(f'Maximum: {float(max(sys.argv))}')
print(f'Mean: {mean: .4f}')
print(f'Std. dev: {sd: .3f}')
print(f'Median: {median: .3f}')


"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
