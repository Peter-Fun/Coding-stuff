class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * target
        dp.insert(0,1)
        for i in range(len(dp)):
            for n in nums:
                if i + n < len(dp):
                    dp[i+n] += dp[i]
        return dp[target]
