class Solution(object):
    def maxScore(self, C, K):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        best = total = sum(C[:K])
        for i in range (K-1, -1, -1):
            total += C[i + len(C) - K] - C[i]
            best = max(best, total)
        return best
