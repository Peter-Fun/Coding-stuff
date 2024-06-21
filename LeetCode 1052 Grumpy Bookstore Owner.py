class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        total = 0
        prefix = [0]
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total += customers[i]
                prefix.append(prefix[-1])
            else:
                prefix.append(prefix[-1] + customers[i])
        maxi = 0
        for i in range(minutes, len(customers)+1):
            if prefix[i] - prefix[i-minutes] > maxi:
                maxi = prefix[i] - prefix[i-minutes]
        return total + maxi
