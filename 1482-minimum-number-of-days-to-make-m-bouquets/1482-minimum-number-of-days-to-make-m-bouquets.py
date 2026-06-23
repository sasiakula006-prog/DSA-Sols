class Solution(object):
    def minDays(self, bloomDay, m, k):
        n = len(bloomDay)
        def check(t):
            cnt = 0
            tb = 0
            for i in range(n):
                if bloomDay[i]<=t:
                    cnt +=1
                else:
                    tb += (cnt//k)
                    cnt = 0
            tb += cnt//k
            if tb>=m:
                return True
            return False
        
        md = max(bloomDay)
        l = 1
        h = md
        ans = -1
        while l<=h:
            mid = (l+h)//2
            if check(mid):
                ans = mid
                h = mid-1
            else:
                l = mid+1
        return ans
        