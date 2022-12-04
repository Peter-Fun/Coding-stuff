class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        last = sum(nums)
        ans = 9999999
        index = 0
        for i in range(len(nums)):
            if i == len(nums)-1:
                if sum(nums)//len(nums) < ans:
                    index = len(nums)-1
            else:
                first += nums[i]
                last -= nums[i]

                if abs(first//(i+1) - last // (len(nums)-i-1)) < ans:
                    index = i
                    ans = min(ans,abs(first//(i+1) - last // (len(nums)-i-1)))
                print(first//(i+1))
                print(last // (len(nums)-i-1))
        return index
