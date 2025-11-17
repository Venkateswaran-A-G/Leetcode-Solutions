class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)-1
        sum =0
        for i in range(n):
            sum += abs(ord(s[i])-ord(s[i+1]))
        return sum
