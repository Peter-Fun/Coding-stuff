class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort(reverse = True)
        summed = 0
        for i in range(1,len(piles) / 3 * 2, 2):
            summed += piles[i]
        return summed
