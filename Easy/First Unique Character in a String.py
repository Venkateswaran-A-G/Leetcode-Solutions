# Date: 11-11-2026
# Problem Number: 387
# Problem Title: First Unique Character in a String
# LeetCode Link: https://leetcode.com/problems/first-unique-character-in-a-string/description/
# Difficulty: Easy
# Topic: Hashmap
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        if not freq:
            return -1
        else:
            first = ""
            for i in freq.keys():
                if freq[i] == 1:
                    first = i
                    break
            if first == "":
                return -1
            return s.index(first)
        