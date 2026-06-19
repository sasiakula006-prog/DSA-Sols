class Solution(object):
    def lemonadeChange(self, bills):
        n = len(bills)
        d = defaultdict(int)
        for i in range(n):
            d[bills[i]] +=1
            c = bills[i]-5
            if c>=10 and d[10]>=(c//10):
                d[10] -= c//10
                c = c%10
            if c>=5 and d[5]>=(c//5):
                d[5]-=c//5
                c = c%5
            if c:
                return False
        return True    
