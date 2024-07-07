class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        empty = 0
        total = 0
        while numBottles != 0:
            empty += numBottles
            total += numBottles
            numBottles = empty // numExchange
            empty %= numExchange 
        return total
