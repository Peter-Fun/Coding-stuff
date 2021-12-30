class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        n = 1
        for i in range(k):
            remainder = n % k
            if remainder == 0: return i+1
            n = remainder * 10 + 1
        return -1
