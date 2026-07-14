from math import gcd
class Solution(object):
    def subsequencePairCount(self, nums):
        MOD = 1000000007
        n = len(nums)
        m = max(nums)
        if n==1:
            return 0
        dp = [[[-1]*(m+1) for _ in range(m+1)] for _ in range(n)]
        def f(i,g1,g2):
            if i==n or g1>m or g2>m :
                return 0
            if dp[i][g1][g2] !=-1:
                return dp[i][g1][g2]
            p1,p2,p3=(f(i+1,gcd(g1,nums[i]),g2))%MOD,(f(i+1,g1,gcd(g2,nums[i])))%MOD,f(i+1,g1,g2)
            if gcd(g1,nums[i])==g2:
                p1 +=1
            if gcd(g2,nums[i])==g1:
                p2 +=1
            dp[i][g1][g2] = p1+p2+p3
            return p1+p2+p3
        return (f(0,0,0))%MOD