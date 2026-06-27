# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        def lh(n):
            cnt = 0
            while n:
                cnt +=1
                n = n.left
            return cnt
        
        def rh(n):
            cnt = 0
            while n:
                cnt +=1
                n = n.right
            return cnt
        def dfs(cur):
            if not cur:
                return 0
            l = lh(cur)
            r = rh(cur)
            if lh == rh:
                return 2**(lh)-1
            return 1+dfs(cur.left)+dfs(cur.right)
        return dfs(root)