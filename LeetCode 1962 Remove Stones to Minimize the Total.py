class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        q = []
        for x in piles:
            heappush(q, -x)
        while k:
            x = heappop(q)
            heappush(q, x + (-x // 2))
            k -= 1
        return -sum(q)
