class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def works(day):
            count = 0
            bloomed = 0
            for b in bloomDay:
                if b <= day:
                    bloomed += 1
                else:
                    bloomed = 0
                if bloomed == k:
                    count += 1
                    bloomed = 0
            return count >= m
        mini = 0
        maxi = max(bloomDay)
        while mini <= maxi:
            middle = (maxi+mini) / 2
            if works(middle):
                if not works(middle-1):
                    return middle
                maxi = middle-1
            else:
                mini = middle + 1
        return -1

        
