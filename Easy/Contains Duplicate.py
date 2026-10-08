# Date: 08-10-2026
# Problem Number: 217
# Problem Title: Contains Duplicate
# LeetCode Link: https://leetcode.com/problems/contains-duplicate/description/
# Difficulty: Easy
# Topic: Set
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!= len(set(nums))
