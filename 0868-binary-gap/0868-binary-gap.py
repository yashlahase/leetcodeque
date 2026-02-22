class Solution(object):
    def binaryGap(self, n):
        b = bin(n)[2:]
        last = None
        max_gap = 0

        for i in range(len(b)):
            if b[i] == '1':
                if last is not None:
                    max_gap = max(max_gap, i - last)
                last = i

        return max_gap