class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        maximum = 0
        curr = 0
        for i in gain:
            curr += i
            if curr > maximum:
                maximum = curr
        return maximum
