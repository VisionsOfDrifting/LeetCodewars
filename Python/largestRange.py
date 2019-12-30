"""Problem:
   Given an array of integers, return the largest range, inclusive,
   of integers that are all included in the array.

   For example, given the array [9, 6, 1, 3, 8, 10, 12, 11], return (8, 12)
   since 8, 9, 10, 11, and 12 are all in the array.

   [9, 6, 1, 3, 8, 10, 12, 11]
   [1, 3, 6, 8, 9, 10, 11, 12]

   Approach:
   To determine a range we will look at the elements in the array
   and check to see if they are in our dictionary.
   As we access the elements in the dictionary we will remove them.
   If the element is in the dictionary then we have an element
   in a new range we have not yet looked at.
   We have a base case, a range of one element.
   We must also check all sequential elements greater than
   or less than this given element.
   By doing so we keep track of the smallest value in the range as
   well as the largest value in the range and the size of the range.
   Each iteration of the for loop effectively computes a new unique range.
   Once all the unique ranges in the array have been found the dictionary
   will be empty and the loop terminates.
"""


def compute_largest_range(arr):
    print(arr)

    # Generate the hash map: O(n)
    d = {i: True for i in arr}
    print(d)

    # Initialize local auxiliary variables
    largest_range = (-1, -1)
    max_range = -1

    # Compute the ranges: O(n)
    for i in arr:
        # Break the loop if d is empty
        if len(d) == 0:
            break

        # Check if the element is still in d, it may not be after the first loop
        if i in d:
            print("%s in dictionary" % i)
            del d[i]
            local_max_range = 1

            # Look for smaller elements
            smaller = i - 1
            while smaller in d:
                print("%s in dictionary (smaller)" % smaller)
                del d[smaller]
                local_max_range = local_max_range + 1
                smaller = smaller - 1

            # Look for larger elements
            larger = i + 1
            while larger in d:
                print("%s in dictionary (larger)" % larger)
                del d[larger]
                local_max_range = local_max_range + 1
                larger = larger + 1

        # Each iteration of the loop compare if the new range is larger
        if local_max_range > max_range:
            max_range = local_max_range
            largest_range = (smaller + 1, larger - 1)

        print(d)
        print("current max_range: %s" % max_range)
        print(largest_range)

    print(max_range)
    return largest_range


# input = [9, 6, 3, 8, 10, 12, 11]
input = [16, 1, 12, 5, 4, 10, 2, 11, 13, 3, 15]
output = compute_largest_range(input)
# output should be a tuple (8, 12)
