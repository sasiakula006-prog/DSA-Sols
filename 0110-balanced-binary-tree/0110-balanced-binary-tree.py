# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        self.c = True
        def dfs(cur):
            if not cur:
                return 0
            l = 1+dfs(cur.left)
            r = 1+dfs(cur.right)
            if abs(r-l)>1:
                self.c = False
            return max(l,r)
        l = dfs(root)
        return self.c