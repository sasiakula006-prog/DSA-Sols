# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        d = {}
        q = deque([(root,0)])
        while q:
            n,v = q.popleft()
            if not n:
                continue
            if v not in d:
                d[v] = n.val
            q.append((n.right,v+1))
            q.append((n.left,v+1))
        
        ans = []
        for i in sorted(d.keys()):
            ans.append(d[i])
        return ans