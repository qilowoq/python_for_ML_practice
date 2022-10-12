# title Sum of diagonal elements
# description Найти сумму элементов на главной и побочной диагоналях
#in:
#mat = [[1,2,3],
#       [4,5,6],
#       [7,8,9]]
#  
#out: 
#25  
#---end---

def diagonalSum(mat):
    sum = 0
    n = len(mat)
    for i in range(n):
        if i != n - 1 - i:
            sum += mat[i][i] + mat[i][n-1-i]
        else:
            sum += mat[i][i] 
    return sum