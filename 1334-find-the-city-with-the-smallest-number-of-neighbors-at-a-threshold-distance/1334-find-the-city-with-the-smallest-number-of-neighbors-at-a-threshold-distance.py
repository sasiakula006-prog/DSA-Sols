class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        dis = [[distanceThreshold+1]*n for _ in range(n)]
        adj = defaultdict(list)
        nv = [n]*n
        min_vis = 0
        for u,v,d in edges:
            adj[u].append((v,d))
            adj[v].append((u,d))
        for i in range(n):
            h = [(0,i)]
            dis[i][i] = 0
            vis = set()
            while h:
                d1,v1 = heapq.heappop(h)
                if d1>distanceThreshold :
                    continue
                for v2,d2 in adj[v1]:
                    if d1+d2 <dis[i][v2] and d1+d2 <=distanceThreshold:
                        dis[i][v2] = d1+d2
                        if v2 not in vis:
                            vis.add(v2)
                        heapq.heappush(h,(dis[i][v2],v2))
            nv[i] = len(vis)
            if nv[i]<= nv[min_vis]:
                min_vis = i
        return min_vis
        
            