class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        taken = [False] * (2*100000+1)
        needed = []
        total = 0
        for i in range(len(nums)):
            if taken[nums[i]]:
                needed.append(nums[i])
            else:
                taken[nums[i]] = True
        print(needed)
        needed.sort()
        for i in range(len(taken)):
            if needed == []:
                break
            if needed[0] < i and not taken[i]:
                total += i - needed[0]
                del needed[0]
        return total
