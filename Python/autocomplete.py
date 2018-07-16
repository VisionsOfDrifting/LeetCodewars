"""Problem:
   This problem was asked by Twitter.
   Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, 
   return all strings in the set that have s as a prefix.
   For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
   Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""
#I had no idea what a Trie was untill I got this problem
#This is also trivia like. Its pretty impossible to implement a trie in interview time limit,
#so I'm assuming that the question is whether or not you know what it is and how you'd call its functions.
import trie

def autocomplete(qS, S):
   dictionary = trie.Trie()
   for word in S: dictionary.add(word)
   return dictionary.start_with_prefix(qS)
   
qS = "de"
S = ["dog", "deer", "deal"]
autoCompletedS = autocomplete(qS, S)
print(autoCompletedS)