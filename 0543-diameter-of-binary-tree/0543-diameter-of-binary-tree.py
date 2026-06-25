# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.d = 0
        def dfs(cur):
            if not cur:
                return -1
            l = 1+dfs(cur.left)
            r = 1+dfs(cur.right)
            self.d = max(self.d,l+r)
            return max(l,r)
        a = dfs(root)
        return self.d