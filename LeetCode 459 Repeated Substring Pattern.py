class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1,len(s)):
            if s[0:i] * (len(s) // i) == s:
                return True
        return False
