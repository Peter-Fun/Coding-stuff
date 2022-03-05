class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right = 0,len(height)-1
        mxArea = 0
        while left<right:
            mxArea = max(mxArea, min(height[left],height[right])*(right-left))
            if height[left]>height[right]: 
                right-=1
            else: 
                left+=1
        return mxArea
