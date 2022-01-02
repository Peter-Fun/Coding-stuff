class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        occurences = {}
        for t in time:
            try:
                occurences[t%60] += 1
            except:
                occurences[t%60] = 1
        
        works = 0
        for i in range(60):
            try:
                if i == 0 or i == 30:
                    works += occurences[i] * (occurences[i]-1)
                else:
                    works += occurences[i] * occurences[(60-i) % 60]
            except:
                pass
        return works //2 
