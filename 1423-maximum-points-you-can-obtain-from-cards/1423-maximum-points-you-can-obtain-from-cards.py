class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        r = n-1
        maxi = 0
        t = sum(cardPoints[:k])
        maxi =max(maxi,t)
        for l in range(k-1,-1,-1):
            t += (-cardPoints[l]+cardPoints[r])
            r -=1
            maxi = max(maxi,t)
        return maxi