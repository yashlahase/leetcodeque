class Solution(object):
    def minBitwiseArray(self, nums):
        ans = []
        for p in nums:
            if p == 2:
                ans.append(-1)
                continue

            best = None
            for x in range(p):  # p <= 1000, brute force is fine
                if (x | (x + 1)) == p:
                    best = x
                    break

            ans.append(best if best is not None else -1)
        return ans
