class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cases = ["1"]
        for i in range(n):
            say = cases[-1]
            said = ""
            curr = ""
            length = 0
            for j in range(len(say)):
                if curr == "" or say[j] == curr:
                    curr = say[j]
                    length += 1
                else:
                    said = said + str(length) + curr
                    curr = say[j]
                    length = 1
            said = said + str(length) + curr
            cases.append(said)
        return cases[n-1]
