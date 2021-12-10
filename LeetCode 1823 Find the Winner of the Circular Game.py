class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        liste = [i for i in range(1,n+1)]
        k = k-1
        offset = k
        while len(liste) > 1:
            liste.pop(offset)
            offset = (offset+k) % len(liste)
        return liste[0]
