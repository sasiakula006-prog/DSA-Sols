class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        parent = [i for i in range(n)]
        
        for u in range(1,n):
            if nums[u]-nums[u-1]<=maxDiff:
                parent[u] = parent[parent[u-1]]
            
        ans = []
        for u1,v1 in queries:
            if parent[u1]==parent[v1]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
