class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        a = [(nums[i],i) for i in range(n)]
        a.sort(key = lambda x:x[0])
        pos = [0]*n
        for i in range(n):
            pos[a[i][1]] = i
        
        sft = [[0]*(18) for _ in range(n)]

        l = 0
        for r in range(n):
            while a[r][0] - a[l][0]>maxDiff:
                sft[l][0] = r-1
                l+=1
        while l<n:
            sft[l][0] = n-1
            l+=1
        
        for j in range(1,18):
            for i in range(n):
                sft[i][j] = sft[sft[i][j-1]][j-1]
        
        ans = [-1]*(len(queries))

        for i,(u,v) in enumerate(queries):
            a,b = pos[u],pos[v]
            if a>b:
                a,b = b,a
            if a==b:
                ans[i] = 0
                continue            
            cur = a
            s = 0
            for j in range(17,-1,-1):
                if sft[cur][j]<b:
                    cur = sft[cur][j]
                    s += 2**j
            if sft[cur][0] >= b:
                ans[i] = s+1
            else:
                ans[i] = -1
        return ans