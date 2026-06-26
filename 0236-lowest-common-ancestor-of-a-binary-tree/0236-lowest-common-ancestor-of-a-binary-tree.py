# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def dfs(cur):
            if not cur:
                return 
            if cur == p or cur==q:
                return cur
            l = dfs(cur.left)
            r = dfs(cur.right)
            if l and r :
                return cur
            if l:
                return l
            if r:
                return r
        return dfs(root)

        