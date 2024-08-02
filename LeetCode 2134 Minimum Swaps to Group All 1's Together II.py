class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = nums.count(1)
        nums.extend(nums)
        maxi = 0
        currcount = nums[:total].count(1)
        for i in range(len(nums)-total):
            if currcount > maxi:
                maxi = currcount
            currcount -= nums[i]
            currcount += nums[i+total]
        return total - maxi
