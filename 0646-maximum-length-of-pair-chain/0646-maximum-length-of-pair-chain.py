class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x:(x[0],x[1]))
        n = len(pairs)
        dp = [[-1]*n for _ in range(n)]
        if n==1:
            return 1
            
        def f(i,p):
            if i==n:
                return 0
            if dp[i][p] !=-1:
                return dp[i][p]
            if pairs[p][-1] >= pairs[i][0]:
                dp[i][p] = max(f(i+1,p),f(i+1,i))
            else:
                dp[i][p] = max(1+f(i+1,i),f(i+1,p))
            return dp[i][p]

        return f(1,0)+1
            