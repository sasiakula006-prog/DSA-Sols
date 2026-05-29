'''class Unionset:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n

    def find(self,i):
        if i == self.parent[i]:
            return i
        else:
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]

    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv :
            return 
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]'''











class Solution(object):
    def largestIsland(self, grid):
        m,n = len(grid),len(grid[0])
        dic = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i,j,b):
            t = 1
            for di,dj in dic:
                ni,nj = i+di,j+dj
                if 0<=ni<m and 0<=nj<n:
                    if grid[ni][nj]==1:
                        grid[ni][nj]=-1
                        t+=dfs(ni,nj,b)
                    elif grid[ni][nj]==0:
                        b.add((ni,nj))
            return t
        zeros = defaultdict(int)
        maxi = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    grid[i][j] = -1
                    boundaries = set()
                    size = dfs(i,j,boundaries)
                    maxi = max(maxi,size)
                    for z in boundaries:
                        zeros[z]+=size
        if len(zeros):
            return max(zeros.values())+1
        else:
            return maxi








        '''m,n = len(grid),len(grid[0])
        og = Unionset(m*n)
        dic = [(0,1),(1,0),(-1,0),(0,-1)]
        zeros = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==0:
                    zeros.append((i,j))
                    continue
                u = (i*n) + j
                for di,dj in dic:
                    ni,nj = i+di,j+dj
                    if 0<=ni<m and 0<=nj<n and grid[ni][nj]==1:
                        v = (ni*n)+nj
                        og.union(u,v)
        if not zeros:
            return og.size[og.find(0)]
        ans = 1
        for i,j in zeros:
            vis = set()
            for di ,dj in dic:
                ni,nj = i+di,j+dj
                if 0<=ni<m and 0<=nj<n and grid[ni][nj]==1:
                        node = (ni*n)+nj
                        vis.add(og.find(node))
            a=1
            for p in vis:
                a+= og.size[p]
            if ans<a:
                ans =a  

        return ans'''