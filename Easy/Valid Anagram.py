# Date: 09-10-2026
# Problem Number: 242
# Problem Title: Valid Anagram
# LeetCode Link: https://leetcode.com/problems/valid-anagram/description/
# Difficulty: Easy
# Topic: Hash Map
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        word_count = {}
        for i in s:
            if i in word_count:
                word_count[i]+=1
            else:
                word_count[i]=1
        for i in t:
            if i in word_count:
                word_count[i]-=1
            else:
                word_count[i]=-1
        for i in word_count.values():
            if i<0 or i > 0:
                return False
        return True