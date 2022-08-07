class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[1,1,1,1,1]]
        for i in range(1,n):
            liste = []
            liste.append(dp[i-1][1] + dp[i-1][4] + dp[i-1][2])
            liste.append(dp[i-1][0] + dp[i-1][2])
            liste.append(dp[i-1][1] + dp[i-1][3])
            liste.append(dp[i-1][2])
            liste.append(dp[i-1][2] + dp[i-1][3])
            dp.append(liste[:])
        return sum(dp[-1]) % (10**9+7)
