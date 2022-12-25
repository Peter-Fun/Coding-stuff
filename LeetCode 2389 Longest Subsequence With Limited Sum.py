class Solution(object):
    def answerQueries(self, nums, queries):
        nums.sort()
        preSum = [0]
        for n in nums:
            preSum.append(preSum[-1]+n)
        res = []
        for q in queries:
            indx = bisect_right(preSum,q)
            res.append(indx-1)
        return res
