from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            s = target - nums[i]
            if s in dict:
                return [dict[s],i]
            dict[nums[i]] = i

l = [3,3]
s = Solution()
t = 6
print(s.twoSum(l,t))