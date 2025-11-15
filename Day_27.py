class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num = set()
        n = len(nums)
        dup = 0
        for number in nums:
            if number in num:
                dup = number
            num.add(number)
        exp_sum = (n*(n+1))//2
        actual_sum = sum(num)
        miss = exp_sum - actual_sum
        return [dup,miss]
