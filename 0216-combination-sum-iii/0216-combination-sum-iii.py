class Solution(object):
    def combinationSum3(self, k, n):
        L = []
        def orey(s,k,n,j):
            if k==0 and n==0:
                L.append(s)
                return 
            if k==0 or n<=0:
                return 
            for i in range(j,10):
                if i>n:
                    break
                orey(s+[i],k-1,n-i,i+1)
        orey([],k,n,1)
        return L

        