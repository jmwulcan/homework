# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library
n = 5 #I want it to return n, 1+2+3+4+5, 1*2*3*4*5
run_sum = 0
fac = 1
for i in range(1, n+1):
	run_sum += i #running sum
	fac = fac * i # factorial
print(n, end = ' ')
print(run_sum, end = ' ')
print(fac, end = ' ')



"""
python3 22sumfac.py
5 15 120
"""
