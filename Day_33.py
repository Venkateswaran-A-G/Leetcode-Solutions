class Solution:
    def reverse(self, x: int) -> int:
        x1 = str(abs(x))
        x2 = x1[::-1]
        res = int(x2)
        if x < 0:
            res = -res
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
