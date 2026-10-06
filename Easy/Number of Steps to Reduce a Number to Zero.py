# Date: 06-10-2026
# Problem Number: 1342
# Problem Title: 	Number of Steps to Reduce a Number to Zero
# LeetCode Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
# Difficulty: Easy
# Topic: Math, Odd or Even
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num > 0:
            if num%2==0:
                num = num/2
            else:
                num = num-1
            step+=1
        return step
