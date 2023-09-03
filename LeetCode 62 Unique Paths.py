class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m -= 1
        n -= 1
        total = m+n
        if m > n:
            t = m
            m = n
            n = t
        amount = 1
        while total > n:
            amount *= total
            total -= 1
        for i in range(1,m+1):
            amount /= i
        return amount
