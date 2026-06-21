class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])
        ans = [intervals[0]]
        for i in range(len(intervals)):
            if ans[-1][-1] >= intervals[i][0]:
                if ans[-1][-1] < intervals[i][1]:
                    ans[-1][-1] = intervals[i][1]
            else:
                ans.append(intervals[i])
        return ans