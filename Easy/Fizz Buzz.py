# Date: 06-10-2026
# Problem Number: 412
# Problem Title: Fizz Buzz
# LeetCode Link: https://leetcode.com/problems/fizz-buzz/description/
# Difficulty: Easy
# Topic: Math, String, Simulation
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        ans = []
        for i in range(1,n+1):
            if i % 3 ==0 and i%5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
        
