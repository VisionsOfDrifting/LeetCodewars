"""
A permutation can be specified by an array P, where P[i] represents the
location of the element at i in the permutation. For example, [2, 1, 0]
represents the permutation where elements at the index 0 and 2 are swapped.

Problem:
Given an array and a permutation, apply the permutation to the array.
For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0],
return ["c", "b", "a"].
"""


# I'm not sure if there is some sort of a trick to this...
# This will simply swap in place for an O(n) time and O(1) space solution
def gen_permutation(arr, p):
    # print(arr, p)
    for i in range(len(p)):
        print(arr, p)
        if i != p[i]:
            temp = arr[p[i]]
            arr[p[i]] = arr[i]
            arr[i] = temp
            temp = p[i]
            p[i] = i
            p[temp] = temp
    return arr


input_arr, perumtation = ["a", "b", "c"], [2, 1, 0]
output = gen_permutation(input_arr, perumtation)
print(output)
