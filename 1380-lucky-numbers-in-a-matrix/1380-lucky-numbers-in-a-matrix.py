class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(matrix)):
            minv = 99999999999
            indexv = 0
            for j in range(len(matrix[i])):
                if matrix[i][j] < minv:
                    minv = matrix[i][j]
                    indexv = j
            for k in range(len(matrix)):
                if matrix[k][indexv] >= minv and k != i:
                    break
            else:
                res.append(minv)
        return res
        