class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        a = [-1e4]*(m*n)
        for i in range(m):
            for j in range(n):
                a[(i*n +j+k)%(m*n)] = grid[i][j]
        
        ans = [[-1e4]*n for _ in range(m)]
        for i in range(m*n):
            r = i//n
            c = i%n
            ans[r][c] = a[i]
        
        return ans