from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cmn = ""
        first = strs[0]
        for i in range(len(first)):
            ch = first[i]
            for str in strs:
                if len(str) < i+1:
                    return cmn
                if str[i] != ch:
                    return cmn
            cmn += ch
        return cmn

l = ["flower","flo","floight"]
s = Solution()
print(s.longestCommonPrefix(l))