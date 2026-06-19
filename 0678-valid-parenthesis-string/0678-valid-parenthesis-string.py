class Solution(object):
    def checkValidString(self, s):
        mini,maxi = 0,0
        for val in s:
            if val =='(':
                mini,maxi = mini+1,maxi+1
            elif val =='*':
                mini,maxi = max(0,mini-1),maxi+1
            else:
                if maxi:
                    mini,maxi = max(0,mini-1),maxi-1
                else:
                    return False
        if mini ==0:
            return True
        return False