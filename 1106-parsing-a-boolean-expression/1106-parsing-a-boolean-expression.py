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
            v = []
            i[0]+=1
            while expression[i[0]] !=')':
                if expression[i[0]] != ',':
                    v.append(f(i))
                else:
                    i[0]+=1
            i[0] +=1
            if cur == '&':
                for val in v:
                    if not val:
                        return val
                return True
            if cur == '|':
                for val in v:
                    if val:
                        return val
                return False
            return False
        return f([0])