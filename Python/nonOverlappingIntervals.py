"""Problem:
   Given a collection of intervals, find the minimum number of intervals you need to remove 
   to make the rest of the intervals non-overlapping.
   Note:
   You may assume the interval's end point is always bigger than its start point.
   Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""

import quickSort


def findOverlapping(list: []) -> int:
    if len(list) == 0:
        return 0
    count, current = 0, -float("inf")
    for i in range(len(list)):
        a, b, c = list[i]
        if current > a:
            count += 1
        else:
            current = b
    return count


def intervalLength(a: int, b: int) -> int:
    return b - a


intervals = [[1, 2], [2, 5], [2, 3], [3, 5], [5, 7], [2, 7]]
# intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]  # Should be 1
# intervals = [[1, 2], [1, 2], [1, 2]]  # Should be 2
tuples = []
for i in range(len(intervals)):
    start, end, length = intervals[i][0], intervals[i][1], intervalLength(intervals[i][0], intervals[i][1])
    tuples.append((start, end, length))
print(tuples)
tuples = quickSort.sort(tuples)
print(tuples)
print(findOverlapping(tuples))

"""Questions to ask:
   Are the intervals given in any order
   Is the range -inf to inf
   Runtime? Space? If no requirements try for O(NlogN)
"""

# The key is only doing what the question asks you to do. Don't over think it.
# Here I thought about it in terms of which to delete and created a function
# that was unnecessary to solve the problem. You only need start and end.
# Always remember the trivial case. Always think about edge cases.
