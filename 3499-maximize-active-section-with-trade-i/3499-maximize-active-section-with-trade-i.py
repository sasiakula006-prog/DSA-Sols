class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        cnt1 = 0
        n = len(s)
        for val in s:
            if val =='1':
                cnt1 +=1
        zerob = []
        i=0
        while i<n:
            if s[i] == '0':
                st = i
                while i<n and s[i] == s[st]:
                    i+=1
                zerob.append(i-st)
            i+=1
        if len(zerob) <2:
            return cnt1
        cnt0 = 0
        for i in range(len(zerob)-1):
            cnt0 = max(cnt0,zerob[i]+zerob[i+1])
        return cnt1+cnt0