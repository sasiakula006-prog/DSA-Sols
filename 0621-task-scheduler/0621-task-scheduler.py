class Solution(object):
    def leastInterval(self, tasks, n):
        # using heaps
        '''d = {}
        for val in tasks:
            if val not in d:
                d[val] = 1
            else:
                d[val]+=1
        h = []
        t = 0
        for v,c in d.items():
            heapq.heappush(h,(-c,v))
        while h:
            l = []
            for _ in range(n+1):
                if h:
                    l.append(heapq.heappop(h))
            for c,v in l:
                if c+1 <0:
                    heapq.heappush(h,(c+1,v))
            if h:
                t+= n+1
            else:
                t+= len(l)
        return t'''

        #best sol
        d = {}
        for val in tasks:
            if val not in d:
                d[val]=1
            else:
                d[val]+=1
        mf = max(d.values())
        nmf = 0
        for d in d.values():
            if d == mf:
                nmf +=1
        return max(len(tasks),(mf-1)*(n+1)+nmf)