# Date: 07-10-2026
# Problem Number: 027
# Problem Title: Remove Element
# LeetCode Link: https://leetcode.com/problems/remove-element/description/
# Difficulty: Easy
# Topic: list comprehension
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def removeElement(self, nums, val):
        nums[:] = [n for n in nums if n!=val]
        return len(nums)
