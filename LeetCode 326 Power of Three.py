class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        while not n == 3:
            if n % 3 == 1 or n % 3 == 2:
                return False
            n = n/3

        return True
