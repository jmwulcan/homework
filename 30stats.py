# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

#Calculate count
count=len(sys.argv[1:])

# Calculate mean
sum=0
for i in sys.argv[1:]:
	sum += float(i)
mean=sum/count

#Calculate standard deviation
sum_diff_squared = 0
for i in sys.argv[1:]:
	diff_squared = (float(i) - mean)**2
	sum_diff_squared += diff_squared
sd=	(sum_diff_squared/count)**0.5

#Calculate median - there must be a better way
vec = ''
for i in sys.argv[1:]:
	vec += i
vec_list = list(vec)
vec_list.sort()
if count%2 != 0:
	median_pos = int(len(vec)/2)
	median_list = vec_list[median_pos:median_pos+1]
	median = ''.join(median_list)
	median = int(median)
if count%2 == 0:
	median_pos_low = int(len(vec)/2)
	median_pos_high = int(len(vec)/2)+1
	median_low_list = vec_list[median_pos_low:median_pos_low+1]
	median_high_list = vec_list[median_pos_high:median_pos_high+1]
	median_low = ''.join(median_low_list)
	median_high = ''.join(median_high_list)
	median_low = int(median_low)
	median_high = int (median_high)
	median = median_low + median_high / 2

#Print output
print(f'Count: {count}')
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
