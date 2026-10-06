class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        s,m = 0,0
        for i in accounts:
            for j in i:
                s += j
            m = max(m,s)
            s = 0
        return m
