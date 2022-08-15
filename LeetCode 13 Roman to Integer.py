class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        index = 0
        while True:
            if index >= len(s):
                return num
            if s[index] == "I":
                if index != len(s)-1 and s[index + 1] == "V":
                    num += 4
                    index += 2
                    continue
                elif index != len(s)-1 and s[index + 1] == "X":
                    num += 9
                    index += 2
                    continue
                else:
                    num += 1
            elif s[index] == "V":
                num += 5
            elif s[index] == "X":
                if index != len(s)-1 and s[index + 1] == "L":
                    num += 40
                    index += 2
                    continue
                elif index != len(s)-1 and s[index + 1] == "C":
                    num += 90
                    index += 2
                    continue
                else:
                    num += 10
            elif s[index] == "L":
                num += 50
            elif s[index] == "C":
                if index != len(s)-1 and s[index + 1] == "D":
                    num += 400
                    index += 2
                    continue
                elif index != len(s)-1 and s[index + 1] == "M":
                    num += 900
                    index += 2
                    continue
                else:
                    num += 100
            elif s[index] == "D":
                num += 500
            elif s[index] == "M":
                num += 1000
            index += 1
