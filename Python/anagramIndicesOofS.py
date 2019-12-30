""" Problem:
Given a word w and a string s find all indices in s
which are the starting location of anagrams of w.

The solution below runs in O(s) time and space
"""
from collections import defaultdict


def del_if_zero(d, char):
    if d[char] == 0:
        del d[char]


def anagram_indices(word, s):
    result = []

    freq = defaultdict(int)
    for char in word:
        freq[char] += 1

    print(freq)

    for char in s[:len(word)]:
        freq[char] -= 1
        del_if_zero(freq, char)

    print(freq)

    if not freq:
        result.append(0)

    for i in range(len(word), len(s)):
        print(result)
        start_char, end_char = s[i - len(word)], s[i]
        print(start_char, end_char)
        freq[start_char] += 1
        del_if_zero(freq, start_char)

        freq[end_char] -= 1
        del_if_zero(freq, end_char)
        print(freq)
        if not freq:
            beginning_index = i - len(word) + 1
            result.append(beginning_index)

    return result


# input_word = "ab"
input_word = "ar"
# input_string = "abxaba"
input_string = "abracadabra"
print(input_word, input_string)
output = anagram_indices(input_word, input_string)
print(output)
