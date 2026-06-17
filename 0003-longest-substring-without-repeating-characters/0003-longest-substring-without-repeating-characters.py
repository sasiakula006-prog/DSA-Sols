class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        l=r=0
        d = defaultdict(int)
        maxi = 0
        while r<n:
            if s[r] in d:
                if l<d[s[r]] + 1:
                    l = d[s[r]] + 1
                d[s[r]] = r
                maxi = max(maxi,r-l+1)
            else:
                d[s[r]] = r
                maxi = max(maxi,r-l+1)
            r +=1
        return maxi