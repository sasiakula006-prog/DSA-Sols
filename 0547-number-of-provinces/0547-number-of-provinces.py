class Solution(object):
    def findCircleNum(self, isConnected):
        
        v = set()
        p = 0
        l = len(isConnected)
        def dfs(i):
            v.add(i)
            for j,c in enumerate(isConnected[i]):
                if c==1 and j not in v:
                    dfs(j)
        for i in range(l):
            if i not in v:
                dfs(i)
                p+=1
        return p