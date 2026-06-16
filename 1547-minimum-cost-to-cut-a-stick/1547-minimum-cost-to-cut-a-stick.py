class Solution(object):
    def minCost(self, n, cuts):
        c = len(cuts)
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        l = len(cuts)
        dp = [[-1]*(l) for _ in range(l)]
        def f(i,j):
            if i>j:
                return 0 
            if dp[i][j] !=-1:
                return dp[i][j]
            mini = 1e9
            for k in range(i,j+1):
                s = (cuts[j+1]-cuts[i-1])+f(i,k-1)+f(k+1,j)
                mini = min(s,mini)
            dp[i][j] = mini
            return mini
        return f(1,c)