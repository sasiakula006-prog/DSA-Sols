class Solution(object):
    def minimumTotal(self, triangle):
        d = len(triangle)
        for i in range(1,d):
            for j in range(len(triangle[i])):
                if j and j < len(triangle[i-1]):
                    triangle[i][j] += min(triangle[i-1][j],triangle[i-1][j-1])
                elif j:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += triangle[i-1][j]
        return min(triangle[-1])            