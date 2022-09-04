"""
https://leetcode.com/problems/longest-word-in-dictionary/submissions/

Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

 
"""
from typing import List
import itertools

"""
1- Trie
"""

# class TrieNode:
#     def __init__(self):
#         self.children = collections.defaultdict(TrieNode)
#         self.is_word = False


# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         current = self.root

#         for letter in word:
#             current = current.children[letter]
#         current.is_word = True

#     def search(self, word: str) -> bool:
#         current = self.root
#         for letter in word:
#             # current.children[letter] will always be True
#             current = current.children.get(letter)
#             if current is None:
#                 return False
#         return current.is_word


# class Solution:
#     def longestWord(self, words: List[str]) -> str:

#         t = Trie()
#         for word in words:
#             t.insert(word)

#         ans = []
#         for word in words:
#             is_ans = True
#             for i in range(1, len(word)):
#                 if t.search(word[:i]) is False:
#                     is_ans = False
#                     break

#             if is_ans:
#                 ans.append(word)

#         return max(sorted(ans), key=len) if ans else ""
"""
2 - Iterative

Firstly sort the words to ensure that we iterate in a lexicographical fashion. 

Also, maintain a set of seen words to check whether there is a "path" to the current word we are iterating through. 
We can lengthen the path when we see that there is a previous word that meets the criteria. 
Lastly, in every iteration where there is a path lengthening, check to see if we can update the longest_word.
"""


class Solution(object):
    def longestWord(self, words: List[str]) -> str:
        words.sort()

        words_set, longest_word = set(['']), ''

        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word


"""
3- Crazy Iterative

Triples (missingPrefixes, negatedLength, word) so I can just take the smallest such triple and extract its word. 
I add the empty string to the words so it's there already and beats any word with missing prefixes. 
And accumulate supports strings, giving me all non-empty prefixes (e.g., for "test" it produces "t", "te", "tes" and "test").


"""
# class Solution:
#     def longestWord(self, words: List[str]) -> str:
#         return min(
#                 (set(itertools.accumulate(w)) - set(words), -len(w), w)
#                 for w in words + ['']
#                 )[2]
