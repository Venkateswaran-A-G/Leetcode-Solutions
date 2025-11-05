class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pos = 2
        for i in range(2,len(nums)):
            if nums[i]!=nums[pos-2]:
                nums[pos]=nums[i]
                pos+=1
        return pos