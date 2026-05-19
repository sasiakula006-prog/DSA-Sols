class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        #bfs
        '''ans=[]
        d = [0]*numCourses
        for a,_ in prerequisites:
            d[a]+=1
        ans =[a for a in range(numCourses) if d[a]==0]
        q = deque(ans)
        while q:
            node = q.popleft()
            for a,b in prerequisites:
                if b==node:
                    d[a]-=1
                    if d[a]==0:
                        ans.append(a)
                        q.append(a)
        if len(ans) != numCourses:
            return []
        return ans'''
        vis = [False]*numCourses
        path = [False]*numCourses
        adj = [[] for _ in range(numCourses)]
        ans = []
        for val in prerequisites:
            adj[val[-1]].append(val[0])
        def dfs(i):
            vis[i]= path[i]= True
            for val in adj[i]:
                if not vis[val]:
                    if dfs(val):
                        return True
                elif path[val]:
                    return True
            path[i] = False
            ans.append(i)
            return False
        for i in range(numCourses):
            if not vis[i]:
                if dfs(i):
                    return []
        return ans[::-1]
