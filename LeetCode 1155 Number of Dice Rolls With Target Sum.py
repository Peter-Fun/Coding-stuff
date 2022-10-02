class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        def helper(h, d, target):
            # if target is too small or if it is out of range
            if target <= 0 or target > (d * f):
                return 0
            if d == 1:
                return 1        # no need to check if target is within reach; already done before
            if (d, target) in h:
                return h[(d, target)]        # directly access from hash table
            res = 0
            for i in range(1, f + 1):
                res += helper(h, d - 1, target - i)       # check all possible combinations
            h[(d, target)] = res
            return h[(d, target)]
        
        h = {}
        return helper(h, d, target) % (10 ** 9 + 7)
