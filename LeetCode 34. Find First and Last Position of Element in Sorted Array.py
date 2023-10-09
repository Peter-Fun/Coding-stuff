class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums)-1
        beginning = -1
        while start <= end:
            mid = (start+end)/2
            if nums[mid]> target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
            else:
                if mid == 0 or nums[mid-1] != target:
                    print("hey")
                    beginning = mid
                    break
                else:
                    end = mid-1
                print(mid,start,end)
        if beginning == -1:
            return [-1,-1]
        start = 0
        end = len(nums)-1
        ending = -1
        while start <= end:
            mid = (start+end)/2
            if nums[mid]> target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
            else:
                if mid == len(nums)-1 or nums[mid+1] != target:
                    ending = mid
                    break
                else:
                    start = mid+1
        return [beginning,ending]
