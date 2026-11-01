# Date: 01-11-2026
# Problem Number: 049
# Problem Title: Group Anagrams
# LeetCode Link: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Topic: Hashmap
# Time Complexity: O(N.KlogK)
# Space Complexity: O(N.K)

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram = {}
        for word in strs:
            s = "".join(sorted(word))
            if s in anagram:
                anagram[s].append(word)
            else:
                anagram[s] = [word]
        return list(anagram.values())