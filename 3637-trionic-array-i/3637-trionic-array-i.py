class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        i = 0

        # strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False

        # strictly decreasing
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i == n - 1:
            return False

        # strictly increasing again
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1
