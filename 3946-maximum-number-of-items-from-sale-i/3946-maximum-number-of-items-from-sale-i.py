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
        dp = [b//mini for b in range(budget+1)]
        for i in range(n-1,-1,-1):
            ndp = [-1]*(budget+1)
            for b in range(budget+1):
                p1,p2 = dp[b],0
                if b>=items[i][1]:
                    p2 = 1+d[items[i][0]]+dp[b-items[i][1]]
                ndp[b] = max(p1,p2)
            dp = ndp

        return max(dp)