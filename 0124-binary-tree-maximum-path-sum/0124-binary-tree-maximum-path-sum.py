# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.maxi = -1e3
        def dfs(cur):
            if not cur:
                return 0
            l = max(0,dfs(cur.left))
            r = max(0,dfs(cur.right))
            self.maxi = max(self.maxi,l+r+cur.val)
            return cur.val+max(l,r)
        dfs(root)
        return self.maxi