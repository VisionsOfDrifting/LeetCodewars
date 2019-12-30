""" Problem:
Given a word w and a string s find all indices in s
which are the starting location of anagrams of w.

The solution below runs in O(w x s)
"""
from collections import Counter


def is_anagram(s1, s2):
    print(Counter(s1), Counter(s2))
    return Counter(s1) == Counter(s2)


def anagram_indices(word, s):
    result = []
    for i in range(len(s) - len(word) + 1):
        window = s[i:i + len(word)]
        print(i, window)
        if is_anagram(window, word):
            result.append(i)
    return result


input_word = "ab"
input_string = "abxaba"
print(input_word, input_string)
output = anagram_indices(input_word, input_string)
print(output)
