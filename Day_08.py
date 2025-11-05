class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k%len(nums)
        if k == 0:
            return
        nums[:]=nums[-k:]+nums[:len(nums)-k]
        