class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        n = len(time)
        t = [0]*n
        indg = [0]*n
        children = [[] for _ in range(n)]
        for p,u in relations:
            children[p-1].append(u-1)
            indg[u-1]+=1
        q = deque()
        for u in range(n):
            if indg[u]==0:
                q.append(u)
        ans = 0
        while q:
            u = q.popleft()
            ans = max(ans,time[u]+t[u])
            for v in children[u]:
                indg[v]-=1
                t[v] = max(t[v],t[u]+time[u]) 
                if indg[v] ==0:
                    q.append(v)
        return ans
