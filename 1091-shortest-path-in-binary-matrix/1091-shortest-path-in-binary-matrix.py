class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if n==1 and not grid[0][0]:
            return 1
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        di = [(-1,-1),(-1,1),(1,-1),(-1,0),(0,-1),(1,0),(0,1),(1,1)]
        q = deque()
        q.append(((0,0),1))
        grid[0][0]=1
        while q:
            p,l = q.popleft()
            a,b = p
            if (a,b) == (n-1,n-1):
                return l
            for da,db in di:
                na,nb = a+da,b+db
                if 0<=na<n and 0<= nb <n and grid[na][nb] ==0:
                    q.append(((na,nb),l+1))
                    grid[na][nb]=1
        return-1