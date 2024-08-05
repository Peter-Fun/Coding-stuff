class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        unique = []
        for i in arr:
            if arr.count(i) == 1:
                unique.append(i)
        if len(unique) < k:
            return ""
        return unique[k-1]
