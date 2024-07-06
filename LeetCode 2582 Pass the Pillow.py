class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        pattern = time % ((n-1) * 2) # (n-1) * 2 is the amount of passing to reach back to 1
        if pattern >= n: # going backwards is involved
            return 2 * n - (pattern+1)
        else:
            return 1 + pattern
