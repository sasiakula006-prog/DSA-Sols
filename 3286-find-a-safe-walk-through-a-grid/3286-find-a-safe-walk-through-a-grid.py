class Solution(object):
    def findSafeWalk(self, grid, health):
        m,n = len(grid),len(grid[0])
        dic = [(0,1),(1,0),(-1,0),(0,-1)]
        q = deque([(health-grid[0][0],0,0)])
        d = [[0]*n for _ in range(m)]
        d[0][0] = health-grid[0][0]
        while q:
            h,i,j = q.popleft()
            if h<=0:
                continue
            if i==m-1 and j==n-1:
                return True
            for di,dj in dic:
                ni,nj = i+di, j+dj
                if 0<=ni<m and 0<= nj <n and h-grid[ni][nj]>d[ni][nj]:
                    d[ni][nj] = h -grid[ni][nj]
                    q.append((h-grid[ni][nj],ni,nj))

        return False