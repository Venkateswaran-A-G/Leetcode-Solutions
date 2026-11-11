# Date: 11-11-2026
# Problem Number: 409
# Problem Title: Longest Palindrome
# LeetCode Link: https://leetcode.com/problems/longest-palindrome/description/
# Difficulty: Easy
# Topic: Hashmap
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s)==1:
            return 1
        freq={}
        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        result  = 0
        odd = False
        for value in freq.values():
            if value%2 == 0:
                result+=value
            else:
                odd = True
        if odd == False:
            return result
        else:
            for value in freq.values():
                if value % 2==1:
                    result += (value -1)
            return result+1