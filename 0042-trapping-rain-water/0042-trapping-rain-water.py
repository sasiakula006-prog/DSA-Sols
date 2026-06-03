class Solution(object):
    def trap(self, height):
        #brute force
        n = len(height)
        def pme(arr,n):
            pre_max = [0]*n
            pre_max[0] = arr[0]
            for i in range(1,n):
                pre_max[i] = max(pre_max[i-1],arr[i])
            return pre_max


        def nme(arr,n):
            post_max = [0]*n
            post_max[-1] = arr[-1]
            for i in range(n-2,-1,-1):
                post_max[i] = max(post_max[i+1],arr[i])
            return post_max

        NME = nme(height,n)
        PME = pme(height,n)
        area = 0
        for i in range(n):
            area += max(0,min(NME[i],PME[i]) - height[i])
        return area
                
        