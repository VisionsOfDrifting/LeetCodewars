"""
Given a smaller substring and a larger string
find all permutations of the substring in the larger string.
"""
# This question is a brute force O(k!*n) where k is the 
# length of the substring and n is the length of the string.
# You don't want to get stuck into thinking you have to generate permutations
# the best way to do this is to keep track of a window of the frequencies of 
# chars in the larger string. If the window and pattern have the same numbers
# of frequencies then we've found a match. Every iteration we check for match,
# move the window forward one char and recalculate the current frequencies.

# We'd like to take advantage of the fact that there are 256 ascii chars
# and map them accordingly. If you are worried about space you could move
# your mapping by doing 0 => ascii first char to len => ascii first char - ascii last char
# and then change the size of the window and pattern to match the size. 
# You'll have to account for the gaps between continuous character segments as well.

# For example if we are only looking for alphanumerics 256 is rather excessive
# some of these symbols are @, currency symbols, foriegn language symbols, and punctuation
# For nums 0 - 9 are from ascii 48 - 57
# For upper A - Z are from ascii 65 - 90
# For lower a - z are from ascii 97 - 122
# A total of 62 values which means 1/4th the size of the array 
# and 1/4th the ammount of time looping through zeros
# Array would count frequencies [0,...,9,A,...,Z,a,...,z]
#                               [0,...,10,11,...,35,...,61]
# If you'd like you can generate the array described with this code.
"""
chars = []
for i in range(62):
   # This would be best as a switch, but python doesn't have switch statements
   if(i < 10):
      chars.append(chr(ord('0') + i))
   elif(i < 36):
      chars.append(chr(ord('A') - 10 + i))
   elif(i < 62):
      chars.append(chr(ord('a') - 36 + i))

for i in range(62):
   print(i , chars[i])
"""
# The point is 256 is still O(1), but for the vast majority of anagrams this is overkill.
# There is also a point that I like to argue; being that constant time in cases like this 
# will run slower than O(N^2) in examples smaller than 256 - len(pat) characters.
# This algorithm is an example of something that generalizes well and gets all the edge cases, 
# but if you actually had to do this in practice you would need to consider these factors.
# In an interview you would want to mention runtime analysis like this and potential ideas for
# optimization. I would still write this in an interview because it isn't hard to memorize
# and it is a good solution compared to generating the permutations.

# A better solution that I won't take the time to write would be able to dynamically devise
# a mapping between characters given the chars in the pattern. But this seemingly requires
# another algorithm to devise the mapping. You would have to actually do this to see if
# such an algorithm exists that would actually save you time.

MAX=256

# compare the frequency count we are keeping of chars
# if they are the same return true
# This function runs in O(1) because max is a constant
# though I think for smaller examples this is excessive
def compare(arr1, arr2):
   for i in range(MAX):
      if arr1[i] != arr2[i]:
         return False
   return True
    
# Search for all permutations of pat[] in txt[] 
def search(pat, txt):
   M = len(pat)
   N = len(txt)
   # Frequency of chars in pattern
   countP = []
   for i in range(MAX):
      countP.append(0)
   # Frequency of chars in text window
   countTW = []
   for i in range(MAX):
      countTW.append(0)

   for i in range(M):
      (countP[ ord(pat[i]) ]) += 1
      (countTW[ ord(txt[i]) ]) += 1
   # Traverse the characters of pattern
   for i in range(M,N):
      # Compare the frequency counts
      if compare(countP, countTW):
         print("Found at Index", (i-M))
      # Add current character to current window
      (countTW[ ord(txt[i]) ]) += 1
      # Remove the first character of previous window
      (countTW[ ord(txt[i-M]) ]) -= 1
   # Check for the last window in text
   if compare(countP, countTW):
      print("Found at Index", N-M)
       
txt = "BACDGABCDA"
pat = "ABCD"
search(pat, txt)