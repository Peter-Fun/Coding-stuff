class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        dp = [0] * (high + 1)
        dp[0] = 1
        md = 10 ** 9 + 7
        for i in range(min(zero, one), high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % md
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % md

        s = 0
        for i in range(low, high + 1):
            s = (s + dp[i]) % md
        return s

