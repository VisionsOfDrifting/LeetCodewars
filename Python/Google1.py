import re

def qrCode(S,K):
   retString = ""
   retString2 = ""
   S = S.upper()
   #print(S)
   p = re.compile('[A-Z0-9]')
   counter = 0
   for i in range(len(S)-1,-1,-1):
      char = S[i]
      #print(S[i])
      #print(bool(p.match(char)))
      if(bool(p.match(char))):
         if(counter == K):
            counter = 1
            if(K != 0):
               retString += "-"
         else:
            counter += 1
         retString += char
      #print("Counter is:",counter)
   for i in range(len(retString)-1,-1,-1):
      retString2 += retString[i]
   return retString2

print(qrCode('2-4A0r7-4k', 4))
print(qrCode('2-4A0r7-4k', 3))
print(qrCode('r', 1))
print(qrCode('2-4A0r7-4k', 0))

"""
Example test:   ('2-4A0r7-4k', 4)
OK

Example test:   ('2-4A0r7-4k', 3)
OK

Example test:   ('r', 1)
OK
"""