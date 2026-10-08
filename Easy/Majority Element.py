# Date: 08-10-2026
# Problem Number: 169
# Problem Title: Majority Element
# LeetCode Link: https://leetcode.com/problems/majority-element/description/
# Difficulty: Easy
# Topic: Hash Map
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count= {}
        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n] = 1
        max_key = max(count.keys(), key=lambda k: count[k])
        return max_key