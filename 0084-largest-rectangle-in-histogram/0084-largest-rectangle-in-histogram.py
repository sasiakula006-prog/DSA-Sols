class Solution(object):
    def largestRectangleArea(self, heights):
        #brute force
        '''n = len(heights)
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
        return maxi'''
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