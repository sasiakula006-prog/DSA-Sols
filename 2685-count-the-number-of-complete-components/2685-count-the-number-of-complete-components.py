class Solution(object):
    def countCompleteComponents(self, n, edges):
        parent = [i for i in range(n)]
        size = [1]*n
        def find(i):
            if parent[i]==i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(u,v):
            pu = find(u)
            pv = find(v)
            if size[pu]>=size[pv]:
                parent[pv] = pu
                size[pu] +=size[pv]
            else:
                parent[pu] = pv
                size[pv]+=size[pu]



        for u,v in edges:
            if find(u)==find(v):
                continue
            union(u,v)
        
        d = defaultdict(int)
        cnt = 0

        for u,v in edges:
            d[parent[u]]+=1

        for node in range(n):
            if node == parent[node] and size[node]==1:
                cnt+=1
            if node in d and d[node] == (size[node]*(size[node]-1))//2:
                cnt += 1
        return cnt
            