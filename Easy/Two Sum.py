# Date: 08-10-2026
# Problem Number: 001
# Problem Title: Two Sum
# LeetCode Link: https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy
# Topic: Hash Map
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            if nums[i] in diff:
                return [diff[nums[i]],i]
            else:
                diff[target - nums[i]]=i
