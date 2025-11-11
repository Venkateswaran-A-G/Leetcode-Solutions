class Solution:
    def jump(self, nums: List[int]) -> int:
        maxReach = 0
        current = 0
        count = 0
        for i in range(len(nums)-1):
            maxReach= max(maxReach,i+nums[i])
            if i==current:
                count+=1
                current = maxReach
        return count
        
