class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        def f(i):
            j = i
            f = 0
            while j<i+n:
                f += gas[j%n]-cost[j%n]
                if f<0:
                    break
                j+=1            
            return j%n
        
        i = 0
        while i<n:
            if gas[i]>=cost[i]:
                v = f(i)
                if v == i:
                    return i
                if v<i:
                    return -1
                i = v
                continue
            i+=1
        return -1
        
        