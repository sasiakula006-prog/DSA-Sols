class Solution(object):
    def maximumSafenessFactor(self, grid):
        q = deque()
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.append((i,j))

        dic = [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            i,j = q.popleft()
            for di,dj in dic:
                ni,nj = i+di,j+dj
                if 0<=ni<n and 0<= nj<n and not grid[ni][nj]:
                    grid[ni][nj] = grid[i][j]+1
                    q.append((ni,nj))

        h = [(-grid[0][0],0,0)]
        while h:
            sf,i,j = heapq.heappop(h)
            sf *=-1
            if i==n-1 and j == n-1:
                return sf-1
            for di,dj in dic:
                ni,nj = i+di,j+dj
                if 0<=ni<n and 0<= nj<n and grid[ni][nj]>0:
                    heapq.heappush(h,(-1*min(sf,grid[ni][nj]),ni,nj))
                    grid[ni][nj] *=-1
