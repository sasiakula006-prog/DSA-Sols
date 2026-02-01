class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand)%groupSize:
            return False
        d = Counter(hand)
        h = list(d.keys())
        heapq.heapify(h)
        while h:
            f = h[0]
            for i in range(f,f+groupSize):
                if i not in d or d[i]==0:
                    return False
                d[i] -=1
                if d[i] ==0:
                    if i != heapq.heappop(h):
                        return False
        return True
                