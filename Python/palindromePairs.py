""" Problem:
Given a list of words, find all pairs of unique indices such
that the concatenation of the two words is a palindrome.

For example, given the list of ["code", "edoc", "da", "d"],
return [(0,1), (1, 0), (2, 3)]

The solution below runs in O(n^2 * c) time, where m is the
number of words and c is the length of the longest word.
"""


def is_palindrome(word):
    # print(word, word[::-1])
    # Note: word[::-1] is a simple way to reverse a string
    return word == word[::-1]


def palindrome_pairs(words):
    result = []

    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1 + word2):
                result.append((i, j))

    return result


input_list = ["code", "edoc", "da", "d"]
print(input_list)
output = palindrome_pairs(input_list)
print(output)
