"""
Given a list of possibly overlapping intervals, return a new list of 
intervals where all overlapping intervals have been merged.
The input list is not necessarily ordered in any way.
For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], 
you should return [(1, 3), (4, 10), (20, 25)].
"""
# First you want to ask questions about merging. Would merging (1,3),(2,8) => (1,8)
# Assuming so...

for i in N 

N = [(1, 3), (5, 8), (4, 10), (20, 25)];
N2 = [(1, 3), (2, 8), (1, 10), (3, 25)]; # [(1,10),(3,25)]