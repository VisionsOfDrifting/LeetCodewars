"""
Given a list of possibly overlapping intervals, return a new list of 
intervals where all overlapping intervals have been merged.
The input list is not necessarily ordered in any way.
For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], 
you should return [(1, 3), (4, 10), (20, 25)].
"""
# First you want to ask questions about merging. 
# Would merging (1,3),(2,8) => (1,8)
# Assuming so... (c,d),(a,b) => (c,b) d < b
# also consider  (5,11),(4,10) => (4,11)
#                 (c,d),(a,b) => (a,d) c < a
# but the merger above would not happen in a sorted list
#                         (1,3),(4,10) => push
# Only want to push when   (c,d),(a,b) => d < a
# c < d and a < b are always obviously true

# Brute force is obviously to use a double for loop
# A stack will work for an O(nlogn) time and O(n) space because you have to sort
# heapq in python seems to only work for integers
# An O(nlogn) time with O(n) space simply merges the intervals while iterating

from quickSort import sort  # sort takes a list as argument


def overlappingIntervals(N):
    intervals = sort(N)
    print(intervals)
    stack = []
    i = 0
    for a, b in intervals:
        print(stack)
        print(a, b)
        if not stack:
            stack.append((a, b))
            i = i + 1
        c, d = stack[i - 1]
        # Note that these two checks happen concurrently
        # if you put them as separate checks they will have unintended effects
        # because if d is less than a it is implicit that d is also less than b
        if d < a:
            stack.append((a, b))
            i = i + 1
        elif d <= b:
            stack[i - 1] = (c, b)
    return stack


N = [(1, 3), (5, 8), (4, 10), (20, 25)]
N2 = [(1, 3), (2, 8), (1, 10), (3, 25)]  # [(1,25)]
merged = overlappingIntervals(N2)
print(merged)
