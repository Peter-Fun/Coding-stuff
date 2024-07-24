class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """

        def convert(num):
            new = ""
            for i in str(num):
                new += str(mapping[int(i)])
            return int(new)
        for i in range(len(nums)):
            nums[i] = [nums[i],i,convert(nums[i])]
        return [i[0] for i in sorted(nums, key = lambda x: (x[2], x[1]))]
