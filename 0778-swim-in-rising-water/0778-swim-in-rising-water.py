class Solution(object):
    def swimInWater(self, grid):
        n = len(grid)
        dic = [(0,1),(1,0),(-1,0),(0,-1)]
        h = [(grid[0][0],0,0)]
        t=0
        vis = set()
        while h:
            l,i,j = heapq.heappop(h)
            if t<l:
                t=l
            if (i,j)==(n-1,n-1):
                return t
            for di,dj in dic:
                ni,nj = i+di,j+dj
                if 0<=ni<n and 0<=nj<n and (ni,nj) not in vis:
                    heapq.heappush(h,(grid[ni][nj],ni,nj))
                    vis.add((i,j))
        



        