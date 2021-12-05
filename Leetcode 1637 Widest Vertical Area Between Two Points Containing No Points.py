class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(reverse = False, key = lambda x: x[0])
        maxx = 0
        for i in range(len(points)-1):
            if points[i+1][0] - points[i][0] > maxx:
                maxx = points[i+1][0] - points[i][0]
        return maxx
