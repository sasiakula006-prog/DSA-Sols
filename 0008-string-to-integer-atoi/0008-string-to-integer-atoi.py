class Solution(object):
    def myAtoi(self, s):
        sign = 1
        s = s.lstrip()
        a = []
        if len(s) ==0:
            return 0
        if s[0] == "-":
            sign = -1
        elif s[0] == "+":
            sign = 1
        elif s[0].isdigit():
            a.append(int(s[0]))
        else:
            return 0
        for val in s[1:]:
            if val.isdigit():
                a.append(int(val))
            else:
                break
        l = len(a)
        num = 0
        for i in range(l):
            e = l-1-i
            num += a[i]*(10**e)
        num *= sign
        if num < -2**31:
            num = -2**31
        if num >= 2**31:
            num = 2**31 -1 
        return num

        