class Solution(object):
    def lemonadeChange(self, bills):
        f = 0
        t = 0
        for val in bills:
            if val == 5:
                f+=1
            elif val == 10:
                if f:
                    f -=1
                else:
                    return False
                t +=1
            else:
                if t and f:
                    f-=1
                    t-=1
                elif f>=3:
                    f-=3
                else:
                    return False
        return True    
