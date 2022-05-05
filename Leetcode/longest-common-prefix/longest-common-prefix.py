class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = ""
        for num in zip(*strs):
            if len(set(num)) == 1:
               ans += num[0] 
            else:
                return ans
        return ans