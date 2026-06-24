class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0]>target:
                break
            if matrix[i][-1]<target:
                continue
            l1 = 0
            h1 =n-1
            while l1<=h1:
                m1 = (l1+h1)//2
                if matrix[i][m1] ==target:
                    return True
                elif matrix[i][m1]>target:
                    h1 = m1-1
                else:
                    l1 = m1+1
        return False
        