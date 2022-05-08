class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        total = 0
        sums = [0] * len(bank)
        for row in range(len(bank)):
            for cell in bank[row]:
                sums[row] += int(cell)
        for i in range(len(bank)):
            for j in range(i+1, len(bank)):
                if sums[j] > 0:
                    total += sums[i] * sums[j]
                    break
        return total
        
