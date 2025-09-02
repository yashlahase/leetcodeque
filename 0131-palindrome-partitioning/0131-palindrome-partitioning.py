class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        curr_part = []

        def helper(start):
            if start == len(s):
                result.append(curr_part[:])

            for i in range(start,len(s)):
                temp = s[start:i+1]
                if temp == temp[::-1]:
                    curr_part.append(temp)
                    helper(i+1)
                    curr_part.pop()
            
        helper(0)
        return result