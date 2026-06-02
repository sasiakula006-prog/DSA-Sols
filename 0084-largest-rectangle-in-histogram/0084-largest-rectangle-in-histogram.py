class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)
        def nse(arr,n):
            res = [n]*n
            stack = []
            for i in range(n):
                while stack and arr[stack[-1]]>arr[i]:
                    res[stack.pop()] = i
                stack.append(i)
            return res
        
        def pse(arr,n):           
            res = [-1]*n
            stack = []
            for i in range(n):
                while stack and arr[stack[-1]]>arr[i]:
                    stack.pop()
                if stack:
                    res[i] = stack[-1]
                stack.append(i)
            return res
        NSE = nse(heights,n)
        PSE = pse(heights,n)
        maxi = 0
        for i in range(n):
            area = heights[i]*(NSE[i]-PSE[i]-1)
            maxi = max(maxi,area)
        return maxi