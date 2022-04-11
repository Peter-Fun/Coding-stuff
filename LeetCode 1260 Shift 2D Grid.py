class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        for i in range(k):
            row = [0] * len(grid[0])
            new = []
            for j in range(len(grid)):
                new.append(row[:])
            for j in range(len(grid)):
                for l in range(len(grid[0])):
                    new[(j + (l+1)//len(grid[0]))%len(grid)][(l+1)%len(grid[0])] = grid[j][l]
            grid = new[:][:]
        return grid
