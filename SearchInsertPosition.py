from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for x in range(0,len(nums)):
            if target == nums[x]:
                return x
            if target <  nums[x]:
                return x
            if target > nums[len(nums) - 1] and x == len(nums) - 1:
                return x + 1

s = Solution
n = [1,3,5,6]
t = 2
print(s.searchInsert(s,n,t))