class Solution(object):
    def orangesRotting(self, grid):
        q = deque()
        fc = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fc +=1
        if not fc:
            return 0
        t = -1
        while(q):
            t +=1
            for _ in range(len(q)):
                a,b = q.popleft()
                for r,c in [(-1,0),(0,-1),(0,1),(1,0)]:
                    na = a+r
                    nb = b+c
                    if 0<=na<m and 0<= nb <n and grid[na][nb]==1:
                        grid[na][nb]=2
                        q.append((na,nb))
                        fc-=1
        if fc:
            return -1
        return t
