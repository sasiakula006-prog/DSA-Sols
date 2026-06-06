class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        vis = set()
        h = [False]*m
        v = [False]*n
        def horizontal(x):
            h[x] = True
            for j in range(n):
                matrix[x][j]=0
        
        def vertical(y):
            v[y] = True
            for i in range(m):
                matrix[i][y]=0

        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    vis.add((i,j))

        for i,j in vis:
            if not h[i]:
                horizontal(i)
            if not v[j]:
                vertical(j)
        