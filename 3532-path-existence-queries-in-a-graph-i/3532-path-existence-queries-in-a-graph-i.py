class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        size = [1]*n
        parent = [i for i in range(n)]
        def find(i):
            if parent[i]==i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def join(u,v):
            pu = find(u)
            pv = find(v)
            if pu==pv:
                return
            if size[pu]>=size[pv]:
                parent[pv] = pu
                size[pu] += size[pv]
            elif size[pu] < size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]
        
        for u in range(1,n):
            if nums[u]-nums[u-1]<=maxDiff:
                join(u,u-1)
            
        ans = []
        for u1,v1 in queries:
            if find(u1)==find(v1):
                ans.append(True)
            else:
                ans.append(False)
        return ans
