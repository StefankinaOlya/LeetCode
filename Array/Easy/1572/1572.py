class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summa = 0
        minus_arg = 0
        for i in range(len(mat)):
            summa += mat[i][len(mat[i]) - i -1]
            for j in range(len(mat[i])):
                if i == j:
                    print("right diag", mat[i][j])
                    summa += mat[i][j]
                if i == j == (len(mat[i]) - 1) / 2:
                    minus_arg = mat[i][j]
        return summa - minus_arg
