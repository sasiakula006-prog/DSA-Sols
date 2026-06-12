class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        if str1 == str2:
            return str1
        m,n = len(str1),len(str2)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 0
        for i in range(n+1):
            dp[0][i] = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        ans = ""
        i = m
        j = n
        while i>0 and j>0:
            if str1[i-1] == str2[j-1]:
                ans = str1[i-1] + ans
                i -= 1
                j -= 1
            elif dp[i-1][j]>dp[i][j-1]:
                ans = str1[i-1] + ans
                i -=1
            else:
                ans = str2[j-1] + ans
                j-=1
        return str1[:i] + str2[:j] + ans