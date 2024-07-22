class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        people = []
        for i in range(len(names)):
            people.append([heights[i],names[i]])
        people.sort(reverse = True)
        return [i[1] for i in people]
