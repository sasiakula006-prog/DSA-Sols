class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        r = n-1
        maxi = 0
        t = sum(cardPoints[:k])
        maxi =max(maxi,t)
        while k:
            t += (-cardPoints[k-1]+cardPoints[r])
            r -=1
            k -=1
            maxi = max(maxi,t)
        return maxi