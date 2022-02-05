class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = []
        neg = []
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        final = []
        for i in range(len(pos)):
            final.append(pos[i])
            final.append(neg[i])
        return final
