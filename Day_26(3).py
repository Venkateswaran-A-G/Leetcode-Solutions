class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        num1 = nums[:n]
        num2 = nums[n:]
        ans = []
        for i in range(n):
            ans.append(num1[i])
            ans.append(num2[i])
        return ans
