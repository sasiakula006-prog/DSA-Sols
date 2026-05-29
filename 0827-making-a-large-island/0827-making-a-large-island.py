class Unionset:
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
            self.size[pv] += self.size[pu]


class Solution(object):
    def largestIsland(self, grid):
        m,n = len(grid),len(grid[0])
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
        options = defaultdict(set)
        for i,j in zeros:
            for di ,dj in dic:
                ni,nj = i+di,j+dj
                if 0<=ni<m and 0<=nj<n and grid[ni][nj]==1:
                        node = (ni*n)+nj
                        options[(i,j)].add(og.find(node))
        ans = 1
        for val in options.values():
            a=1
            for p in val:
                a+= og.size[p]
            if ans<a:
                ans =a 
        return ans