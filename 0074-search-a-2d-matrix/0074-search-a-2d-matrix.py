class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        l0,l1 = 0,0
        h0,h1 = m-1,n-1
        i = h0
        while l0<=h0:
            m0 = (l0+h0)//2
            if matrix[m0][-1]>=target:
                i = m0
                h0 = m0-1
            else:
                l0 = m0+1

        while l1<=h1:
            m1 = (l1+h1)//2
            if matrix[i][m1] ==target:
                return True
            elif matrix[i][m1]>target:
                h1 = m1-1
            else:
                l1 = m1+1
        return False