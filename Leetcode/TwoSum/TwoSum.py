'https://leetcode.com/problems/two-sum/'

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for k in range(len(nums)) :
            for i  in range(k+1, n):
                if nums[k] + nums[i] == target  :
                    return [k,i]