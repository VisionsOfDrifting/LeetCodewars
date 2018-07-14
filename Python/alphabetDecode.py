"""Problem:
   This problem was asked by Facebook.
   Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
   For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
   You can assume that the messages are decodable. For example, '001' is not allowed.
"""
#This is what I came up with in 35 minutes. It has similar concepts to a good solution
"""
def alphabetDecode(S):
   def decodeHelper(sub):
      count = 0
      if(len(sub) == 1):
         if(int(sub) != 0):
            count += 1
      else: 
         if(int(sub[0]+sub[1])/27 < 1):
            count += 1
      return count
   count = 0
   if(len(S) % 2 == 1): #odd
      for i in range(len(S)):
         if i+1 != len(S):
            count += decodeHelper(S[i:i+1])
         count += decodeHelper(S[i])
   else: #even
"""

def alphabetDecode(S):
   ways = [1,0] #Argument is 1 way to decode empty string...
   print(ways)
   for i in range(len(S)):
      numWays = 0
      #This gets singleton != 0; 1-9
      if(S[i] > '0'):
         numWays += ways[0]
      #This gets 10-19, 20-26
      if(i > 0) and ((S[i-1] == '1') or (S[i-1] == '2' and S[i] < '7')):
         numWays += ways[1]
      ways[1] = ways[0]
      ways[0] = numWays;
      print(ways)
   return ways[0]

#S = '111'
#S = '101'
#S = '126'
S = '1111'
print(S)
print(alphabetDecode(S))

#Getting faster. Need to do more dynamic programming ones.
#Try to figure out your base cases