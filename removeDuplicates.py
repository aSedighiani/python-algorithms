from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = {}
        b = 0
        for x in nums:
            if x not in a:
                a[x] = 1
                b += 1
        nums.clear()
        for key in a:
            nums.append(key)
        return b
        

s = Solution()
input = [0,0,1,1,1,2,2,3,3,4]
result = s.removeDuplicates(input)
print(result)
print(input)