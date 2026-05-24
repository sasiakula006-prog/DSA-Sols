class Solution(object):
    def networkDelayTime(self, times, n, k):
        time = [float('inf') for _ in range(n)]
        adj = defaultdict(list)
        time[k-1]=0
        for u,v,w in times:
            adj[u].append((v,w))
        h = [(0,k)]
        while h:
            t,b = heapq.heappop(h)
            for b1,t1 in adj[b]:
                if t+t1 < time[b1-1]:
                    time[b1-1] = t+t1
                    heapq.heappush(h,(time[b1-1],b1))
        ans = max(time)
        if ans == float('inf'):
            return -1
        return ans
        