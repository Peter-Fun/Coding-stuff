class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        answer = []
        for i in range(len(l)):
            stuff = nums[l[i]:r[i]+1]
            stuff.sort()
            diff = stuff[1]-stuff[0]
            for i in range(2,len(stuff)):
                if stuff[i] - stuff[i-1] != diff:
                    answer.append(False)
                    break
            else:
                answer.append(True)
        return answer
        
