class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        r = n-1
        l = 0
        t = 0
        maxi = 0
        while k:
            t+=cardPoints[l]
            l+=1
            k-=1
        l -= 1
        maxi =max(maxi,t)
        while l>=0:
            t += (-cardPoints[l]+cardPoints[r])
            l -=1
            r -=1
            maxi = max(maxi,t)
        return maxi