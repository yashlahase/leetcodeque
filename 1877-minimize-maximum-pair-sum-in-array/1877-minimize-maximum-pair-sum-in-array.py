class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        n = len(nums)
        ans = 0
        
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n - 1 - i])
        
        return ans
