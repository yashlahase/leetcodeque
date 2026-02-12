class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
            freq = [0] * 26   # frequency array for characters
            
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                
                # collect non-zero frequencies
                counts = [f for f in freq if f > 0]
                
                # check if all frequencies are equal
                if len(set(counts)) == 1:
                    max_len = max(max_len, j - i + 1)

        return max_len
