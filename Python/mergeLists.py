"""Problem:
   return a new sorted merged list from K sorted lists, each with size N.
"""

import heapq


def merge(lists):
    merged_list = []
    # grab the first K elements (lst[0], listsIndex, indexInList)
    heap = [(item[0], i, 0) for i, item in enumerate(lists) if item]
    print(heap)
    # construct heap. This could also be done with heapq.heappush
    heapq.heapify(heap)
    while heap:
        print(heap)
        val, list_ind, element_ind = heapq.heappop(heap)
        print(merged_list)
        merged_list.append(val)
        # as long as there are elements in the list we just appended an element from
        if element_ind + 1 < len(lists[list_ind]):
            # grab another element from the same list and put it on the heap
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list


# lists = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
lists = [[17, 20, 32], [10, 15, 30], [12, 15, 20]]
# lists = [[17, 32, 32], [10, 15, 32], [12, 32, 32]]
# [10, 12, 15, 15, 17, 20, 20, 30, 32]
print(lists)
print(merge(lists))

# enumerate(iterable, start=0)
"""
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
"""
"""
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)
# Output:
# 1 apple
# 2 banana
# 3 grapes
# 4 pear
"""
