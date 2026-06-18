class Solution(object):
    def minWindow(self, s, t):
        d = defaultdict(int)
        for val in t:
            d[val]+=1
        cnt = 0
        n = len(s)
        si = -1
        mini = 1e9
        l = 0
        for r in range(n):
            d[s[r]]-=1
            if d[s[r]] >= 0:
                cnt+=1
            while cnt==len(t):
                if mini>(r-l+1):
                    mini = r-l+1
                    si = l
                d[s[l]]+=1
                if d[s[l]]>0:
                    cnt-=1
                l+=1
        if mini ==1e9:
            return ''
        return s[si:si+mini]