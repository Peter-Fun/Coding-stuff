class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        liste = []
        done = []
        for i in nums:
            if i in done:
                pass
            else:
                done.append(i)
        amounts = []
        for i in done:
            amounts.append(nums.count(i))
        sorte = sorted(amounts,reverse = True)
        for i in range(k):
            liste.append(done[amounts.index(sorte[i])])
            del done[amounts.index(sorte[i])]
            del amounts[amounts.index(sorte[i])]
        return liste
