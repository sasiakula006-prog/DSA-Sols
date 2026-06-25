# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        self.length = 1
        def dfs(cur,l):
            if not cur:
                return 
            self.length = max(self.length,l)
            dfs(cur.left,l+1)
            dfs(cur.right,l+1)
        dfs(root,1)
        return self.length
        