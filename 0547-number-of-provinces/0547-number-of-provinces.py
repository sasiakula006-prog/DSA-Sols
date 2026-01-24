class Solution(object):
    def findCircleNum(self, isConnected):
        visited = set()
        provinces = 0

        def dfs(city):
            visited.add(city)
            for cur, connected in enumerate(isConnected[city]):
                if connected and cur not in visited:
                    dfs(cur)
            
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces += 1

        return provinces
        '''v = set()
        p = 0
        l = len(isConnected)
        def dfs(i):
            v.add(i)
            for j,c in enumerate(isConnected[i]):
                if j==1 and c not in v:
                    dfs(c)
        for i in range(l):
            if i not in v:
                dfs(i)
                p+=1
        return p'''