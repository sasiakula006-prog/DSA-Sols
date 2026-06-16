class Solution(object):
    def parseBoolExpr(self, expression):
        n = len(expression)
        def f(i):
            cur = expression[i[0]]
            i[0]+=1
            if cur =='t':
                return True
            if cur =='f':
                return False
            if cur == '!':
                i[0]+=1
                r = not f(i)
                i[0]+=1
                return r
            has_t = False
            has_f = False
            i[0]+=1
            while expression[i[0]] !=')':
                if expression[i[0]] != ',':
                    v = f(i)
                    if v:
                        has_t = True
                    else:
                        has_f = True
                else:
                    i[0]+=1
            i[0] +=1
            if cur == '&':
                if has_f:
                    return False
                return True
            if cur == '|':
                if has_t:
                    return True
                return False
            return False
        return f([0])