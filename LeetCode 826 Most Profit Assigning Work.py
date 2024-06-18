class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = []
        for i in range(len(difficulty)):
            jobs.append([profit[i],difficulty[i]])
        jobs.sort(reverse = True, key = lambda x: x[0])
        worker.sort(reverse = True)
        profit = 0
        j = 0
        for i in worker:
            while j < len(jobs):
                if i >= jobs[j][1]:
                    profit += jobs[j][0]
                    break
                else:
                    j+= 1
        return profit
