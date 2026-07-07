class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)<sum(cost):
            return -1
        n = len(gas)
        f = 0
        ans = 0
        i = 0
        while i<n:
            f += gas[i]-cost[i]
            if f<0:
                ans = (i+1)
                f = 0
            i+=1
        return ans
        