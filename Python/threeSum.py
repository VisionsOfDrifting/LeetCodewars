""" Problem:
    Given an array (list) of ints, return sets of three 
    numbers that sum to zero. No repeats.
    Solution: 
    Sort the array. Pick the first number, and then set
    the remaining subarray values to point at the leftmost
    and rightmost sides. Continue to try values untill the
    pointers cross or point in the same place; then reccur.
    If a proper set is found add it to our list of solutions.
"""
# Add the ability for script inputed nums and target
# May want to pseudo random generate test sets
   
def threeSum(nums, L, target):
   for i in range (len(nums) - 2):
      if (i = 0 or nums[i] != nums[i-1]):
         left = i + 1
         right = len(nums) - 1
         new_sum = target - nums[i]
         print("i = ",i,"left = ",left,"right = ",right,"new_sum = ",new_sum)
         while(left < right)
            if(nums[left] + nums[right] == new_sum):
               match = [nums[i], nums[left], nums[right]]
               L.append(list(match))
               print("Match Found!")
               print(nums[i]," + ",nums[left]," + ",nums[right]," = ",target)
               #return (L[x], L[target-x])
   #return threeSum(nums[1:], L, target)

nums = [-1, 0, 1, 2, -1, -4]
print(nums)
#quickSort(nums)
#print(nums)
L = []
#L.append(list(a_list)
target = 0
print("target = ", target)
print(threeSum(nums, L, target))

#-1 + 0 + 1 = 0
#-1 + 2 + -1 = 0
