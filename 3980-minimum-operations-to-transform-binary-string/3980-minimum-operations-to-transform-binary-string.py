class Solution(object):
    def minOperations(self, s1, s2):
        n = len(s1)
        inf = float('inf')
        dp = [[-1 for _ in range(2)] for _ in range(n)]
        def dfs(i,b):
            if i == n-1:
                if b==1 and s2[i] == '0':
                    return inf
                if b==0 and s2[i] == '1':
                    return 1
                else:
                    return 0

            if dp[i][b] != -1 :
                return dp[i][b]
            c = 0
            p1,p2 = inf,inf
            if not(b==1 and s2[i]=='0'):
                if b==0 and s2[i]=='1':
                    c+=1
                p1 = c + dfs(i+1,int(s1[i+1]))
            c +=1
            if b==0:
                c +=1
            if s1[i+1] == "0":
                c +=1
            if b==1 and s2[i] == '1':
                c+=1
            p2 = c+dfs(i+1,0)
            dp[i][b] = min(p1,p2)
            return dp[i][b]
        ans = dfs(0,ord(s1[0])-48)
        return (ans if ans != inf else -1)