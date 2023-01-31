from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
    
        for i in range(1,len(nums)):
            if nums[i] != nums[l]:
                l+=1
                nums[l] = nums[i]
        return l + 1
        
s = Solution()
input = [1,1,2]
result = s.removeDuplicates(input)
print(result)
print(input)