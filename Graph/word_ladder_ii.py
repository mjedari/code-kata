"""
https://leetcode.com/problems/word-ladder-ii/


A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].


"""

"""
1- BFS

- To find the shortest path from beginWord to endWord, we need to use BFS.
- To find neighbors of a word, we just try to change each position from the original word, each position we try to change letters from a..z, the neighbors are valid if and only if they're existed in the wordList.
- The problem is required to output the answer sequence paths, so we need to store sequences path so far while doing bfs.
- Let level[word] is the all possible sequence paths which start from beginWord and end at word.
Then level[endWord] is our answer

"""




from typing import List
from string import ascii_lowercase
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # to check if a word is existed in the wordSet, in O(1)
        wordSet = set(wordList)
        wordSet.discard(beginWord)

        def neighbors(word):
            # change every possible single letters and check if it's in wordSet
            for i in range(len(word)):
                for c in ascii_lowercase:
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordSet:
                        yield newWord

        level = {}
        # level[word] is all possible sequence paths which start from beginWord and end at `word`.
        level[beginWord] = [[beginWord]]
        while level:
            nextLevel = defaultdict(list)
            for word, paths in level.items():
                if word == endWord:
                    return paths  # return all shortest sequence paths
                for nei in neighbors(word):
                    for path in paths:
                        # form new paths with `nei` word at the end
                        nextLevel[nei].append(path + [nei])
            # remove visited words to prevent loops
            wordSet -= set(nextLevel.keys())
            level = nextLevel  # move to new level

        return []
