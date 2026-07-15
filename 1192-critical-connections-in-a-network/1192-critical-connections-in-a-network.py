class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[]for _ in range(n)]
        for u,v in connections:
            adj[u].append((v))
            adj[v].append((u))
        time = [-1]*n
        l_time = [-1]*n
        time[0] = l_time[0] = 0
        ans = []
        vis = set()
        def dfs(u,p):
            vis.add(u)
            for v in adj[u]:
                if v==p:
                    continue
                if v not in vis:
                    time[v] = l_time[v] = time[u]+1
                    dfs(v,u)
                    l_time[u] = min(l_time[u],l_time[v])
                    if time[u]<l_time[v]:
                        ans.append([u,v])
                else:
                    l_time[u] = min(l_time[u],l_time[v])
        dfs(0,-1)
        return ans