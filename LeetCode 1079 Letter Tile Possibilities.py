class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        return sum(len(set(itertools.permutations(tiles, i))) for i in range(1, len(tiles) + 1))
