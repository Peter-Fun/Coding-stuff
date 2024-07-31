class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        n = len(books)
        dp = [99999999999] * (n + 1)
        dp[0] = 0  # No books, no height
        
        for i in range(1, n + 1):
            total_thickness = 0
            max_height = 0
            for j in range(i, 0, -1):
                total_thickness += books[j-1][0]
                if total_thickness > shelfWidth:
                    break
                max_height = max(max_height, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1] + max_height)
        
        return dp[n]
