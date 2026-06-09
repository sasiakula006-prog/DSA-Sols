class Solution(object):
    def minimumTotal(self, triangle):
        d = len(triangle)
        '''for i in range(1,d):
            for j in range(len(triangle[i])):
                if j and j < len(triangle[i-1]):
                    triangle[i][j] += min(triangle[i-1][j],triangle[i-1][j-1])
                elif j:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += triangle[i-1][j]
        return min(triangle[-1])'''          
        dp = [[-1]*(i+1) for i in range(d)]
        dp[-1] = triangle[-1][:]
        for i in range(d-2,-1,-1):
            for j in range(i,-1,-1):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j],dp[i+1][j+1])
        return dp[0][0]