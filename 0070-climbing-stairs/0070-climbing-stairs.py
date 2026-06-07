class Solution(object):
    def climbStairs(self, n):
        if n<=2:
            return n
        momo = [0,1,2]
        for i in range(3,n):
            val = momo[i-1]+momo[i-2]
            momo.append(val)
        return momo[n-1]+momo[n-2]
        