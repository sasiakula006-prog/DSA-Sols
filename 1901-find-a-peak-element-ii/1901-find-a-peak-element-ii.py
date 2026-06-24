class Solution(object):
    def findPeakGrid(self, mat):
        m = len(mat)
        n = len(mat[0])
        l = 0
        h = n-1
        def max_r(c):
            maxi = -1
            row = -1
            for i in range(m):
                if mat[i][c]>maxi:
                    maxi = mat[i][c]
                    row = i
            return row
        
        while l<=h:
            mid = (l+h)//2
            r = max_r(mid)
            left = mat[r][mid-1] if mid>0 else -1
            right = mat[r][mid+1] if mid+1<n else -1
            if mat[r][mid]>left and mat[r][mid]>right:
                return [r,mid]
            elif mat[r][mid]<left:
                h = mid-1
            else:
                l =mid+1
        return -1 