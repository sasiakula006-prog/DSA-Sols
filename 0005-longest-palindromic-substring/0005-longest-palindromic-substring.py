class Solution(object):
    def longestPalindrome(self, s):
        if len(s) <=1:
            return s
        ps = s[0]
        def from_centre(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l -=1
                r +=1
            return s[l+1:r]

        for i in range(len(s)-1):
            odd = from_centre(i,i)
            even = from_centre(i,i+1)
            if len(odd) > len(ps):
                ps = odd
            if len(even) > len(ps):
                ps = even
        
        return ps