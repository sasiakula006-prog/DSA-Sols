class Solution(object):
    def numIslands(self, grid):
        m,n = (len(grid),len(grid[0]))
        visted = set()
        di = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j):
            visted.add((i,j))
            for dr,dc in di:
                nr,nc = (i+dr,j+dc)
                if 0<=nr<m and 0<=nc<n and (nr,nc) not in visted and grid[nr][nc]=="1":
                    dfs(nr,nc)
        cont = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in visted:
                    dfs(i,j)
                    cont +=1
        return cont