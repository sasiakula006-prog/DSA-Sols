class Solution(object):
    def characterReplacement(self, s, k):
        n = len(s)
        if n==1:
            return 1
        l = r =0
        maxi = 0
        mf = 0
        d =defaultdict(int)
        while r<n:
            d[s[r]]+=1
            mf = max(mf,d[s[r]])
            while (r-l+1)-mf>k:
                d[s[l]]-=1
                l+=1
            maxi = max(maxi,r-l+1)
            r+=1
        return maxi    
        