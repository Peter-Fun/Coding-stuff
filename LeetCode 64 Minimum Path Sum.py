class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        newgrid = [] #original grid with 0's added to the top and left edges
        dp = [] # best path with minimum sum to get to this spot
        row = [0] * (n+1)
        dprow = [999] * (n+1)
        newgrid.append(row[:])
        dpnewrow = [999] + ([0] * n)
        dp.append(dprow[:])
        for i in range(m):
            newgrid.append([0] + grid[i])
            dp.append(dpnewrow[:])
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 1 and j == 1:
                    dp[i][j] = newgrid[i][j]
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + newgrid[i][j]
        return dp[-1][-1]
