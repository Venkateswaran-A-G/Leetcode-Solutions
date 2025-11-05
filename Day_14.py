class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s ="".join(str(j) for j in digits)
        d = int(s)+1
        dig = [int(i) for i in str(d)]
        return dig
