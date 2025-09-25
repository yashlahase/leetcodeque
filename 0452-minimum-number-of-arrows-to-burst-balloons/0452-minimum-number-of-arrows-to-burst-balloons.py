class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        if not points:
            return 0

        points.sort(key = lambda x : x[1])

        arrow = 1
        arrow_pos = points[0][1]
        
        for start, end in points[1:]:
            if start > arrow_pos:
                arrow += 1
                arrow_pos = end
        
        return arrow



            