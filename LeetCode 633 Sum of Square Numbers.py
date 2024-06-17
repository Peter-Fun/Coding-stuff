class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int(c**0.5)+1):
            new = c - i ** 2
            if new ** 0.5 == int(new**0.5):
                return True

        return False
