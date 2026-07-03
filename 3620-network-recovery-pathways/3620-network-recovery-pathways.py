class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        d = defaultdict(list)
        n = len(online)
        maxc = 0
        for u0,v0,c0 in edges:
            d[u0].append((v0,c0))
            maxc = max(maxc,c0)
        inf = float('inf')
        def check(mc0):
            dis = [inf]*(n)
            dis[0] = 0
            h = [(0,0)]
            while h:
                d0,u= heapq.heappop(h)
                if d0>dis[u]:
                    continue
                if u==n-1:
                    return d0<=k
                for v,c in d[u]:
                    if online[v] and dis[v] > d0+c and c>=mc0:
                        dis[v] = d0+c
                        heapq.heappush(h,(d0+c,v))
            return False
        lo = 0
        hi = maxc
        ans = -1
        while lo<=hi:
            mid = (lo+hi)//2
            if check(mid):
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
        return ans