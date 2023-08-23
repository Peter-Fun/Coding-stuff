import heapq
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        f = [0] * 26
        n = len(s)
        
        for i in range(n):
            f[ord(s[i]) - ord('a')] += 1
            if f[ord(s[i]) - ord('a')] > (n + 1) // 2:
                return ""
        
        p = []
        for i in range(26):
            if f[i] != 0:
                heapq.heappush(p, (-f[i], chr(i + ord('a'))))
        
        ans = []
        while len(p) >= 2:
            freq1, ch1 = heapq.heappop(p)
            freq2, ch2 = heapq.heappop(p)
            ans.extend([ch1, ch2])
            if freq1 < -1:
                heapq.heappush(p, (freq1 + 1, ch1))
            if freq2 < -1:
                heapq.heappush(p, (freq2 + 1, ch2))
        
        if p:
            ans.append(p[0][1])
        
        return ''.join(ans)
