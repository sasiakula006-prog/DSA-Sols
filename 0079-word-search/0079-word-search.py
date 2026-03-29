class Solution(object):
    def exist(self, board, word):
        def bks(h,v,l):
            if l==len(word):
                return True
            if h <0 or h >= len(board) or   v<0 or v >= len(board[0]) or board[h][v]!=word[l]:
                return False
            temp = board[h][v]
            board[h][v] = 0
            if bks(h+1,v,l+1) or bks(h-1,v,l+1) or bks(h,v+1,l+1) or bks(h,v-1,l+1):
                return True
            board[h][v] = temp
        for i in range(len(board)):
                for j in range(len(board[0])):
                    if bks(i,j,0):
                        return True
        return False    
        