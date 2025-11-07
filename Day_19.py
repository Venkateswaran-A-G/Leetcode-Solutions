class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        low = 0
        high = len(numbers)
        while low<=high:
            if (numbers[low]+numbers[high-1])==target:
                return [low+1,high]
            elif (numbers[low]+numbers[high-1])<target:
                low+= 1
            elif (numbers[low]+numbers[high-1])>target:
                high-= 1