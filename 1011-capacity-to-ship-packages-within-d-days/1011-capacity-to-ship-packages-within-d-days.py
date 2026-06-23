class Solution(object):
    def shipWithinDays(self, weights, days):
        n = len(weights)
        def check(c):
            td = 0
            w = 0
            for i in range(n):
                if w+weights[i]>c:
                    td+=1
                    w = weights[i]
                else:
                    w+=weights[i]
            td+= (w+c-1)//c
            if td<=days:
                return True
            return False

        l = max(weights)
        a = (n+days-1)//days
        h = max(weights)*a
        ans = h
        while l<=h:
            m = (l+h)//2
            if check(m):
                ans = m
                h = m-1
            else:
                l = m+1
        return ans
