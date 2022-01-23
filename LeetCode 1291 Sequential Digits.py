class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        digits = "123456789"
        answer = []
        for i in range(len(str(low)), len(str(high)) + 1):
            for j in range(0, 10 - i):
                num = int(digits[j: j + i])
                if num >= low and num <= high:
                    answer.append(num)
        return answer
