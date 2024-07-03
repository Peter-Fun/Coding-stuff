class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 4:
            return 0
        nums.sort()
        minimums = nums[:4]
        maximums = nums[-4:]
        print(len(nums))
        return (min([abs(maximums[i]-minimums[i]) for i in range(len(minimums))]))
        
