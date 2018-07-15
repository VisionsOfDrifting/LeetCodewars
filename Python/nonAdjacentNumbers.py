"""Problem:
   This problem was asked by Airbnb.
   Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
   Numbers can be 0 or negative.
   For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
   [5, 1, 1, 5] should return 10, since we pick 5 and 5.
   Follow-up: Can you do this in O(N) time and constant space?
"""

"""
def sumNonAdjacent(nums):
   sum1, sum2 = 0
   if(len(nums) == 2):
      return 0
   for i in range(0,len(nums),2):
      if(len(nums) - i == 4):
         return sum1 + nums[i] + nums[i+3]
      sum1 += nums[i]
   return sum1
"""

def sumNonAdjacent(nums):
   dp = [nums[0],nums[1]]
   for i in range(2,len(nums),1):
      temp = dp[1]
      dp[1] = dp[0] + nums[i]
      dp[0] = max(dp[0],temp)
      print(dp, nums[i], i)
   return max(dp[0],dp[1])

#nums = [2, 4, 6, 2, 5]
#nums = [5, 1, 1, 5] 
nums = [5, 1, 1, 5, 1, 5] 
#nums = [5, 1, 5, 1, 1, 5] 
#nums = [1,1]
#nums = [1]
#nums = []
print(nums)
print(sumNonAdjacent(nums))

#Need to read the question better missed largest
#This is actually dynamic programming and I missed it
