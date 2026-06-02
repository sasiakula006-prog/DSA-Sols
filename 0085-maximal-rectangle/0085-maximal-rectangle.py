class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)
        stack = []
        maxi = 0
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                a = stack.pop()
                pse = -1
                if stack:
                    pse = stack[-1]
                area = heights[a]*(i-pse-1)
                maxi = max(maxi,area)
            stack.append(i)
        while stack:
            nse = n
            a = stack.pop()
            pse = -1
            if stack:
                pse = stack[-1]
            area = heights[a]*(nse-pse-1)
            maxi = max(maxi,area)
        return maxi
    def maximalRectangle(self, matrix):
        max_a =0
        m = len(matrix)
        n = len(matrix[0])
        h = [0]*n
        for r in range(m):
            for c in range(n):
                if matrix[r][c]=='1':
                    h[c] +=1
                else:
                    h[c] =0
            area = self.largestRectangleArea(h)
            max_a = max(max_a,area)
        return max_a
        