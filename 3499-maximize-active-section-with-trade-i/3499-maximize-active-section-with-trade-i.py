class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        cnt1,cnt0 = 0,0
        n = len(s)
        for val in s:
            if val =='1':
                cnt1 +=1
        i=0
        p = float('-inf')
        while i<n:
            if s[i] == '0':
                st = i
                while i<n and s[i] == s[st]:
                    i+=1
                c = i - st
                cnt0 = max(cnt0,p+c)
                p = c
            i+=1
        return cnt1+cnt0