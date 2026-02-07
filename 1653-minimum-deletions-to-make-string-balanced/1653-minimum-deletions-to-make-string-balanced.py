class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0   # minimum deletions needed so far
        b_count = 0     # number of 'b's seen so far

        for ch in s:
            if ch == 'b':
                b_count += 1
            else:  # ch == 'a'
                # Option 1: delete this 'a'  → deletions + 1
                # Option 2: delete all previous 'b's → b_count
                deletions = min(deletions + 1, b_count)

        return deletions
