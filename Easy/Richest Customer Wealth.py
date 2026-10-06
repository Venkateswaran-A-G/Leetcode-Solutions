# Date: 06-10-2026
# Problem Number: 1672
# Problem Title: Richest Customer Wealth
# LeetCode Link: https://leetcode.com/problems/richest-customer-wealth/description/
# Difficulty: Easy
# Topic: Summation, Max Function
# Tim  e Complexity: O(N²)
# Space Complexity: O(1)

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        s,m = 0,0
        for i in accounts:
            for j in i:
                s += j
            m = max(m,s)
            s = 0
        return m
