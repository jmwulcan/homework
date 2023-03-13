# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

vals = sys.argv[1:] # grab values from command line into list
vals.sort() # sort in order
nums=len(vals) #Calculate count
mid = nums // 2 # find middle position

# Calculate mean
tot = 0
for val in vals:
	tot += float(val)
mean = tot/nums

# Calculate median
if nums %2 != 0:
	median = float(vals[mid])
else:
	median = (float(vals[mid])*2+1)/2

#Calculate standard deviation
sum_diff_squared = 0
for val in vals:
	diff_squared = (float(val) - mean)**2
	sum_diff_squared += diff_squared
sd = (sum_diff_squared/nums)**0.5




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
