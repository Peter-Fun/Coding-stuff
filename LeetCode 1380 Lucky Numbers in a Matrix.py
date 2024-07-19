class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        returned = []
        columns = []
        for i in range(len(matrix[0])):
            col = []
            for j in range(len(matrix)):
                col.append(matrix[j][i])
            columns.append(col[:])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min(matrix[i]) and matrix[i][j] == max(columns[j]):
                    returned.append(matrix[i][j])
        return returned
