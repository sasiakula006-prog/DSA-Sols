class Solution(object):
    def sumAndMultiply(self, n):
        y = 0
        s = 0
        while n:
            a = n%10
            if a:
                s+=a
                y = y*10+a
            n = n//10

        x=0
        while y:
            x = x*10+(y%10)
            y = y//10
            
        return x*s