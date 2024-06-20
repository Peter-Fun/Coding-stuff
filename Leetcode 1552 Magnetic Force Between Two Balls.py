class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        def works(x):
            curr = position[0]
            count = 1
            for p in position[1:]:
                if p - curr >= x:
                    count += 1
                    curr = p
            return count >= m
        mini = 0
        maxi = max(position)
        position.sort()
        while mini <= maxi:
            x = (mini + maxi) / 2
            if works(x):
                if not works(x+1):
                    return x
                mini = x + 1
            else:
                maxi = x - 1
        return -1
