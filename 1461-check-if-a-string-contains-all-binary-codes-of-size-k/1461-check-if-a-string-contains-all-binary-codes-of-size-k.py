class Solution(object):
    def hasAllCodes(self, s, k):
        # total binary codes of length k
        needed = 1 << k   # 2^k
        
        seen = set()
        
        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])
            
            # early stop if all codes found
            if len(seen) == needed:
                return True
        
        return False