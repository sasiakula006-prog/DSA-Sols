class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        price = [float('inf') for _ in range(n)]
        adj = defaultdict(list)
        for a,b,p in flights:
            adj[a].append((b,p))
        q = deque([(0,src,0)])
        while q:
            p0,a1,t = q.popleft()
            if t>k:
                continue
            for b1,p1 in adj[a1]:
                if p0+p1 < price[b1] and t<=k:
                    price[b1] = p0+p1
                    q.append((price[b1],b1,t+1))
        if price[dst]<float('inf'):
            return price[dst]
        return -1
