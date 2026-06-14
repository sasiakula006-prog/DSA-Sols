class Solution(object):
    def longestStrChain(self, words):
        n = len(words)
        words = sorted(words, key=len)
        def check(i,p):
            if len(words[p]) != len(words[i])-1:
                return False
            for j in range(len(words[i])):
                if words[i][:j]+words[i][j+1:]==words[p]:
                    return True
            return False
        maxi = 0
        dp = [1]*n
        for i in range(n):
            for p in range(i):
                if check(i,p) and dp[i]<1+dp[p]:
                    dp[i] = 1+dp[p]
            if dp[i]>maxi:
                maxi = dp[i]
        return maxi