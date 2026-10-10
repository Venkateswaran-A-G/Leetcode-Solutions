# Date: 09-10-2026
# Problem Number: 347
# Problem Title: Top
# LeetCode Link: https://leetcode.com/problems/top-k-frequent-elements/description/
# Difficulty: Medium
# Topic: Hashmap, Min Heap
# Time Complexity: O(N log K)
# Space Complexity: O(M+N)

from heapq import heappush as hp
from heapq import heappop as hpop
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        min_heap = []
        for key, value in freq.items():
            hp(min_heap,[value,key])
            if len(min_heap)>k:
                hpop(min_heap)
        result = []
        for i in min_heap:
            result.append(i[1])
        return result