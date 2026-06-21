class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x:x[-1])
        cnt = 0
        pet = -1e6
        for st,et in intervals:
            if st>=pet:
                pet = et
            else:
                cnt +=1
        return cnt 