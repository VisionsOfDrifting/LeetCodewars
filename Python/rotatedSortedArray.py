"""Problem: 
   Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
   (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
   You are given a target value to search. 
   If found in the array return its index, otherwise return -1.
   You may assume no duplicate exists in the array.
   Your algorithm's runtime complexity must be in the order of O(log n).
"""

def findTarget(array,target):
   low,high = 0,len(array)-1
   while low <= high:
      mid = (low+high)/2
      print("index: ",low,mid,high)
      print("value: ",array[low],array[mid],array[high])
      if array[mid] == target:
         return mid
      elif array[mid] > target:
         if array[high] > array[mid] or array[low] <= target:
            high = mid -1
         else:
            low = mid + 1
      else:
         if array[low] < array[mid] or array[high] >= target:
            low = mid + 1
         else:
            high = mid -1
   print("index: ",low,mid,high)
   return -1
   
array = [4,5,6,7,0,1,2]
print(array)
target = 3
print(target)
print(findTarget(array,target))

#Don't forget about >Binary Search