class Solution(object):
    def climbStairs(self, n):
        if n<2:
            return n
        momo = [1,1]
        for i in range(2,n):
            val = momo[i-1]+momo[i-2]
            momo.append(val)
        return momo[n-1]+momo[n-2]
        