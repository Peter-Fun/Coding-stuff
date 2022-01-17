class Solution(object):
    def countPalindromicSubsequence(self, s):
        return sum(map(lambda i: len(set(s[s.index(i)+1:s.rindex(i)])), set(s)))
