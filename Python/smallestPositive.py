"""Problem: This problem was asked by Stripe.
   Given an array of integers, find the first missing positive integer in linear 
   time and constant space. In other words, find the lowest positive integer that does 
   not exist in the array. The array can contain duplicates and negative numbers as well.
   For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
   You can modify the input array in-place.
"""
# I give up on this one. If someone finds a solution for O(1) space comment on GitHub.



def smallestPositive(N):
   retVal = 1
   positives = []
   for i in range(len(N)):
      if(N[i] > 0):
         print(N[i])
         positives.append(N[i])
   D = dict(zip(positives, range(len(positives))))
   print(positives)
   print(D)
   for i in range(len(positives)):
      if(retVal in D):
         print(retVal,"is in our map")
         retVal += 1
   return retVal


#N = [3,4,-1,0]
#N = [1,2,0]
N = [3,4,-1,0,1,2,6]
print(N)
print("Smallest Positive: ",smallestPositive(N))

#I didn't get this one fast enough. It took four solutions to find one that ran in O(N)
#I didn't read constant space for the first solution

"""Swap in python is as simple as:
   a = 2
   b = 3
   print a, b
   a, b = b, a
   print a, b

   Try it!
"""