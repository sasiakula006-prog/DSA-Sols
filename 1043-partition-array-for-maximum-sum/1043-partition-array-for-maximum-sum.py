class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        n = len(arr)
        dp = [-1]*n
        def f(i):
            if i == n:
                return 0
            if dp[i] !=-1:
                return dp[i]
            maxi = 0
            mx = 0
            for j in range(i,i+k):
                if j<n:
                    mx = max(mx,arr[j])
                    s = mx*(j-i+1) + f(j+1)
                    maxi = max(maxi,s)
            dp[i] = maxi
            return maxi
        return f(0)