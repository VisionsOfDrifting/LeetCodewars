"""Problem: cons(a, b) constructs a pair, and car(pair) and 
   cdr(pair) returns the first and last element of that pair. 
   Given this implementation of cons:
   def cons(a, b):
       def pair(f):
           return f(a, b)
       return pair
   Implement car and cdr.
   Note: This question seems to be trivia/ do you know what a lambda is
"""

def cons(a, b):
   def pair(f):
      return f(a, b)
   return pair

def car(pair):
   return pair(lambda p, q: p)

def cdr(pair):
   return pair(lambda p, q: q)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
