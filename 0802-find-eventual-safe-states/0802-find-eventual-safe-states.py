class Solution(object):
    def eventualSafeNodes(self, graph):
        n= len(graph)
        vis = [False]*n
        path = [False]*n
        ans = []
        def dfs(i):
            vis[i] = path[i] = True
            for val in graph[i]:
                if not vis[val]:
                    if dfs(val):
                        return True
                elif path[val]:
                    return True
            path[i] = False
            ans.append(i)
            return False
        for i in range(n):
            if not vis[i]:
                dfs(i)
        ans.sort()
        return ans
