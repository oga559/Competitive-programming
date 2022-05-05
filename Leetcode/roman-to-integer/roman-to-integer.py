'https://leetcode.com/problems/roman-to-integer/'

class Solution:
    def romanToInt(self, s: str) -> int:
        dic =  {'IV':4,
                'IX':9,
                'XL':40,
                'XC':90,
                'CD':400,
                'CM':900,
                'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000,}
        ans = 0
        for key,val in dic.items():
            cnt = s.count(key)
            ans += cnt * val
            s = s.replace(key, "")
        return(ans)