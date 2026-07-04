class Solution(object):
    def minScore(self, n, roads):
        g = defaultdict(list)
        for u0,v0,d0 in roads:
            g[u0].append((v0,d0))
            g[v0].append((u0,d0))
        minp = float('inf')
        vis = set()
        q = deque([1])
        while q:
            u = q.popleft()
            for v,d in g[u]:
                minp = min(minp,d) 
                if v not in vis:
                    vis.add(v)
                    q.append(v)

        return minp
                    