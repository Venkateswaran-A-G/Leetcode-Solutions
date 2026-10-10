# Date: 10-10-2026
# Problem Number: 125
# Problem Title: Valid Palindrome
# LeetCode Link: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Topic: Two Pointer Technique
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left<right:
            if s[left].isalnum() == False:
                left +=1
            elif s[right].isalnum() == False:
                right-=1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left+=1
                right-=1
        return True