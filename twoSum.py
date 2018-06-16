""" Problem:
    Given an array (list) of ints, return indicies of the
    two numbers such that they add up to a specific target.
    Solution: 
    Walk through the array (list) and compare target minus
    current value with a hash-map (dictionary) of values 
    to indicies. If a match is found return it's indicies 
    otherwise return "No Match".
"""
# Add the ability for script inputed nums and target
# May want to pseudo random generate test sets

def twoSum(nums, D, target):
   if(len(nums) == 1):
      return "No Match"
   x = nums[0]
   print("nums = ",nums)
   if(target-x in D):
      print("Match Found!")
      print(x," + ",target-x," = ",target)
      return (D[x], D[target-x])
   return twoSum(nums[1:], D, target)

nums = [1, 7, 11, 15]
print(nums)
D = dict(zip(nums, range(len(nums))))
print(D)
target = 23
print("target = ", target)
print(twoSum(nums, D, target))