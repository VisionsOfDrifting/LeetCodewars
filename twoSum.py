#Add the ability for script inputed nums and target
#May want to pseudo random generate test sets

def twoSum(nums, D, target):
   if(len(nums) == 1):
      print("No Match")
      return 
   x = nums[0]
   print("nums = ",nums)#,"D = ",D,"x = ",x)
   if(target-x in D):
      print("Match Found!")
      print(x," + ",target-x," = ",target)
      return (D[x], D[target-x])
   return twoSum(nums[1:], D, target)

nums = [1, 7, 11, 15]
print(nums)
D = dict(zip(nums, range(len(nums))))
print(D)
target = 22
print("target = ", target)
print(twoSum(nums, D, target))