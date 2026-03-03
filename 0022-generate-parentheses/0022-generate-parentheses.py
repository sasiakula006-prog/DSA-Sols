class Solution(object):
    def generateParenthesis(self, n):
        n*=2
        s = ''
        c = 0
        L =[]
        self.closedP(L,s,n,c)
        return L
    
    def closedP(self,L,s,n,c):
        s += '('
        c+=1
        n-=1
        if c<0:
            return
        if n ==0:
            if c==0:
                L.append(s)
                return
            else:
                return
        else:
            self.closedP(L,s,n,c)
            self.openedP(L,s,n,c)
        
    def openedP(self,L,s,n,c):
        s+=')'
        c-=1
        n-=1
        if c<0:
            return
        if n ==0:
            if c==0:
                L.append(s)
                return
            else:
                return
        else:
            self.closedP(L,s,n,c)
            self.openedP(L,s,n,c) 

        