class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key = lambda x: x[1])
        print(pairs)
        curr = -99999999999999
        count = 0
        for i in range(len(pairs)):
            if pairs[i][0] > curr:
                curr = pairs[i][1]
                count += 1
        return count 
