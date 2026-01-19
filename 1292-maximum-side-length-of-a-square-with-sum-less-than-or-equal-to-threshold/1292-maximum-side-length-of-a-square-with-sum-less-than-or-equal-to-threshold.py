class Solution(object):
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])

        # Build prefix sum matrix (m+1 x n+1)
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        # Helper to get sum of sub-square using prefix sum
        def get_sum(r1, c1, r2, c2):
            return (
                prefix[r2][c2]
                - prefix[r1][c2]
                - prefix[r2][c1]
                + prefix[r1][c1]
            )

        # Check if any square of side length k has sum <= threshold
        def possible(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    total = get_sum(i, j, i + k, j + k)
                    if total <= threshold:
                        return True
            return False

        # Binary search for maximum k
        low, high = 0, min(m, n)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if possible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
