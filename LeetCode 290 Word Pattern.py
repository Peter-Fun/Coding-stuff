class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        parts = {
            
        }
        for word in range(len(words)):
            try:
                if parts[pattern[word]] != words[word]:
                    return False
            except:
                parts[pattern[word]] = words[word]
        return len(set(parts.values())) == len(list(parts.values()))
