class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x:x[1],reverse=1)
        s=0
        for i,j in boxTypes:
            i=min(i,truckSize)
            s+=i*j
            truckSize-=i
            if truckSize==0:
                break
        return s
