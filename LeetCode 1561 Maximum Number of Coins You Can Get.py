class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        return sum(sorted(piles,reverse = True)[1:len(piles) * 2 / 3 + 1:2])
