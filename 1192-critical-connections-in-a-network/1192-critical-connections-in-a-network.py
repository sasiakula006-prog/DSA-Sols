class Solution(object):
    def criticalConnections(self, n, connections):
        if len(connections) <= n-1:
            return connections
        adj = [[] for _ in range(n)]
        for u0,v0 in connections:
            adj[u0].append(v0)
            adj[v0].append(u0)
        time = [1]*n
        l_t = [1]*n
        vis = [False]*n
        ans = []
        def dfs(u,p):
            vis[u] = True
            for v in adj[u]:
                if v==p:
                    pass
                elif not vis[v]:
                    l_t[v] = time[v] = time[u]+1
                    dfs(v,u)
                    l_t[u] = min(l_t[u],l_t[v])
                    if time[u]<l_t[v]:
                        ans.append([u,v])
                else:
                    l_t[u] = min(l_t[u],l_t[v])
        dfs(0,-1)
        return ans


        