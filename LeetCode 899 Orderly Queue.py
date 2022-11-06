class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k > 1:
            return "".join(sorted(s))
        least = s
        for i in range(len(s)):
            s = s[1:] + s[0]
            if s < least:
                least = s
        return least
