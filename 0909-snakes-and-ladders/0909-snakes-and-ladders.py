class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        b = [0]
        for i in range(n-1,-1,-1):
            if (n-1-i)%2==0:
                for j in range(n):
                    b.append(board[i][j])
            else:
                for j in range(n-1,-1,-1):
                    b.append(board[i][j])
        q = deque([1])
        m = 0
        vis  = set()
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr==n**2:
                    return m
                for v in range(curr+1,min(curr+6,n**2)+1):
                    if v not in vis:
                        vis.add(v)
                        if b[v] ==-1:
                            q.append(v)
                        else:
                            q.append(b[v])
            m+=1
        return -1