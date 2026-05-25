class Solution(object):
    def countPaths(self, n, roads):
        adj = defaultdict(list)
        time = [float('inf')]*n
        for u,v,t in roads:
            adj[u].append((v,t))
            adj[v].append((u,t))
        count = [1]*n
        h = [(0,0)]
        while h:
            t1,v1 = heapq.heappop(h)
            for v2,t2 in adj[v1]:
                if t1+t2 < time[v2]:
                    time[v2]=t1+t2
                    count[v2] = count[v1]
                    heapq.heappush(h,(time[v2],v2))
                elif t1+t2==time[v2]:
                    count[v2] += count[v1]
        return (count[n-1])%(10**9 + 7)
        