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
        dp = [[-1]*n for _ in range(n)]
        def f(i,p):
            if i==n:
                return 0
            a = f(i+1,p)
            if dp[i][p+1] !=-1:
                return dp[i][p+1]
            if p==-1 or check(i,p):
                a = max(a,1+f(i+1,i))
                dp[i][p+1] = a
            return a
        return f(0,-1)