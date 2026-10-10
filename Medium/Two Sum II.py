# Date: 10-10-2026
# Problem Number: 167
# Problem Title: Two Sum II - Input Array Is Sorted
# LeetCode Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Difficulty: Medium
# Topic: Two Pointer Technique
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers)
        while low<=high:
            if (numbers[low]+numbers[high-1])==target:
                return [low+1,high]
            elif (numbers[low]+numbers[high-1])<target:
                low+= 1
            elif (numbers[low]+numbers[high-1])>target:
                high-= 1