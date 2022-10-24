class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        n = len(arr)
        res = [""]
        op = 0
        
        for word in arr:
            for r in res:
                newRes = r+word
                if len(newRes)!=len(set(newRes)): continue
                res.append(newRes)
                op = max(op, len(newRes))
        return op
