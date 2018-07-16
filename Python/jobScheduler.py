"""Problem:
   This problem was asked by Apple.
   Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

from time import sleep
def callFAfterN(f,n):
   sleep(n/1000.0)
   return f()

def twoSquared():
   return 2**2

print(callFAfterN(twoSquared, 10000))

#Some of these are just trivia...