# Date: 07-10-2026
# Problem Number: 088
# Problem Title: Merge Sorted Array
# LeetCode Link: https://leetcode.com/problems/merge-sorted-array/description/
# Difficulty: Easy
# Topic: List Slicing, Concat operation
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m] +nums2
        nums1.sort()