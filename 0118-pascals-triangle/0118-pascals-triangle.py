class Solution(object):
    def generate(self, numRows):
        ans = [[1]*i for i in range(1,numRows+1)]
        if numRows<=2:
            return ans
        for i in range(2,numRows):
            l = len(ans[i])
            for j in range(1,l-1):
                ans[i][j] = ans[i-1][j-1]+ans[i-1][j]
        return ans
        