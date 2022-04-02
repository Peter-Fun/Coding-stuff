class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        
        first = 0
        last = len(s)-1
        while True:
            if s[first] != s[last]:
                remove_l = s[:last] + s[last+1:]
                remove_f = s[:first] + s[first+1:]
                
                return remove_l == remove_l[::-1] or remove_f == remove_f[::-1]
            first +=1
            last -=1

        
