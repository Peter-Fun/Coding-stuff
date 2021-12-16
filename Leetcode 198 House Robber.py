class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        nums.append(0)
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        for i in range(1,len(dp)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        print(dp)
        return dp[len(nums)-1]
