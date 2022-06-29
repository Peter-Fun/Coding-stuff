class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for h, k in sorted(people, key=lambda x: (-x[0], x[1])):
            result.insert(k, [h, k])
        return result
