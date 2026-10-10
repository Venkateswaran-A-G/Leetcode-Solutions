# Date: 10-10-2026
# Problem Number: 283
# Problem Title: Move Zeroes
# LeetCode Link: https://leetcode.com/problems/move-zeroes/description/
# Difficulty: Easy
# Topic: Two Pointer Technique
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left  = 0
        right = len(nums)
        while left<right:
            if nums[left] == 0:
                temp = nums.pop(left)
                nums.append(temp)
                right-=1
            else:
                left+=1
