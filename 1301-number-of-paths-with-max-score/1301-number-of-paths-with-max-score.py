class Solution(object):
    def pathsWithMaxScore(self, board):
        n = len(board)
        mod = 10**9 + 7
        dic = [(1,0),(0,1),(1,1)]
        dp = [[[-1,0]]*n for _ in range(n)]
        dp[-1][-1] = [0,1]
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if board[i][j]=='S' or board[i][j] == 'X':
                    continue
                for di,dj in dic:
                    ni,nj = i+di,j+dj
                    if min(ni,nj)<0 or max(ni,nj)>=n or dp[ni][nj][0] == -1:
                        continue
                    if dp[ni][nj][0] > dp[i][j][0]:
                        dp[i][j] = dp[ni][nj][:]
                    elif dp[ni][nj][0] == dp[i][j][0]:
                        dp[i][j][-1] += dp[ni][nj][-1]
                if dp[i][j][0] !=-1:
                    dp[i][j][0] += (0 if board[i][j]=='E' else int(board[i][j]))

        return ([int(dp[0][0][0]%mod),int(dp[0][0][-1]%mod)] if dp[0][0][0] != -1 else [0,0])