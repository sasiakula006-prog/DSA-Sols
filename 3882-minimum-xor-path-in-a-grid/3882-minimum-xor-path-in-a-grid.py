class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dic = [(0,1),(1,0)]

        dp = [[set() for _ in range(n)] for _ in range(m)]
        vis = set()
        def dfs(i,j):
            vis.add((i,j))
            if i== m-1 and j ==n-1:
                dp[i][j].add(grid[i][j])
                return
            for (di,dj) in dic:
                ni,nj = i+di,j+dj
                if 0<=ni<m and 0<= nj<n:
                    if not (ni,nj) in vis:
                        dfs(ni,nj)
                    for b in dp[ni][nj]:
                        dp[i][j].add(grid[i][j]^b)

        dfs(0,0)
        return min(dp[0][0])
            