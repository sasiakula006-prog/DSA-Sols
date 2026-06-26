# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        q = deque([root])
        ans = []
        c = 0
        while q:
            l = []
            for _ in range(len(q)):
                n = q.popleft()
                l.append(n.val) 
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            if c%2:
                l.reverse()    
            ans.append(l)
            c+=1
        return ans
        