class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        if n ==1:
            return 1
        left = [1]*n
        right = [1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                left[i] = left[i-1]+1
        
        for i in range(n-2,-1,-1):
            if ratings[i]> ratings[i+1]:
                right[i] = right[i+1]+1
        t = 0
        for i in range(n):
            t += max(left[i],right[i])

        return t