import heapq

class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0

        # Doubly linked list pointers
        prev = [-1] * n
        nxt = [-1] * n
        alive = [True] * n

        for i in range(n):
            prev[i] = i - 1
            nxt[i] = i + 1 if i + 1 < n else -1

        # Helper to check non-decreasing in current linked list
        def is_sorted():
            i = 0
            while prev[i] != -1:
                i = prev[i]
            while nxt[i] != -1:
                j = nxt[i]
                if nums[j] < nums[i]:
                    return False
                i = j
            return True

        # Min heap of (sum, left_index)
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        ops = 0

        # Start node (head)
        head = 0
        while prev[head] != -1:
            head = prev[head]

        # Count "bad" places where nums[next] < nums[curr]
        bad = 0
        i = head
        while nxt[i] != -1:
            j = nxt[i]
            if nums[j] < nums[i]:
                bad += 1
            i = j

        while bad > 0:
            # Get valid minimum pair
            while True:
                s, i = heapq.heappop(heap)
                j = nxt[i]
                if j == -1:
                    continue
                if not (alive[i] and alive[j]):
                    continue
                if nums[i] + nums[j] != s:
                    continue
                break

            j = nxt[i]

            # Before merge, remove bad contributions around i and j
            pi = prev[i]
            nj = nxt[j]

            # pairs affected: (pi,i), (i,j), (j,nj)
            if pi != -1 and alive[pi]:
                if nums[i] < nums[pi]:
                    bad -= 1
            if nums[j] < nums[i]:
                bad -= 1
            if nj != -1 and alive[nj]:
                if nums[nj] < nums[j]:
                    bad -= 1

            # Merge i and j into i
            nums[i] = nums[i] + nums[j]
            alive[j] = False

            # Remove j from list
            nxt[i] = nj
            if nj != -1:
                prev[nj] = i

            ops += 1

            # After merge, add new bad contributions around i
            pi = prev[i]
            ni = nxt[i]

            if pi != -1 and alive[pi]:
                if nums[i] < nums[pi]:
                    bad += 1
            if ni != -1 and alive[ni]:
                if nums[ni] < nums[i]:
                    bad += 1

            # Push updated adjacent sums involving i
            if pi != -1 and alive[pi]:
                heapq.heappush(heap, (nums[pi] + nums[i], pi))
            if ni != -1 and alive[ni]:
                heapq.heappush(heap, (nums[i] + nums[ni], i))

        return ops
