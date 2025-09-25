class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """

        n = len(target)

        operation = target[0]

        for i in range(1,n):
            if target[i] > target[i-1]:
                operation += target[i] - target[i-1]

        return operation
        