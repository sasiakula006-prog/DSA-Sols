class Solution(object):
    def maximumSaleItems(self, items, budget):
        d = defaultdict(int)
        n = len(items)
        items.sort(key = lambda x: x[0])
        mini = 1501
        for i in range(n):
            mini = min(mini,items[i][1])
            if items[i][0] in d:
                continue
            for j in range(i+1,n):
                if items[j][0]%items[i][0]==0:
                    d[items[i][0]]+=1
        dp = [[-1]*(budget+1) for _ in range(n)]
        def f(i,b):
            if i==n:
                return b//mini
            if dp[i][b] !=-1:
                return dp[i][b]
            p1,p2 = f(i+1,b),0
            if b>=items[i][1]:
                p2 = 1+d[items[i][0]]+f(i+1,b-items[i][1])
            dp[i][b] = max(p1,p2)
            return max(p1,p2)
        return f(0,budget)