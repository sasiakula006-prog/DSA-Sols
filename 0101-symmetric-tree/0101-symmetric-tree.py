# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        def dfs(c1,c2):
            if not c1 and not c2:
                return True
            if not c1 and c2:
                return False
            if not c2 and c1:
                return False
            if c1.val != c2.val:
                return False
            return dfs(c1.left,c2.right) and dfs(c1.right,c2.left)

        return dfs(root.left,root.right)
            