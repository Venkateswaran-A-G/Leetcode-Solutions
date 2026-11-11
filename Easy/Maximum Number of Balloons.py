# Date: 11-11-2026
# Problem Number: 1189
# Problem Title: Maximum Number of Balloons
# LeetCode Link: https://leetcode.com/problems/maximum-number-of-balloons/description/
# Difficulty: Easy
# Topic: Hashmap
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {"b":0,"a":0,"l":0,"o":0,"n":0}
        for char in text:
            if char in ["b","a","l","o","n"]:
                balloon[char] +=1
        result = []
        for key, value in balloon.items():
            if key in ["b","a","n"]:
                result.append(value)
            else:
                result.append(value//2)
        if not result:
            return 0
        else:
            return min(result)