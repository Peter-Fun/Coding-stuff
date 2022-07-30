class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        ans = set(words1)
        letters = {}
        for i in words2:
            for j in i:
                count = i.count(j)
                if j not in letters or count > letters[j]:
                    letters[j] = count
        for i in words1:
            for j in letters:
                if i.count(j) < letters[j]:
                    ans.remove(i)
                    break
        return list(ans)
