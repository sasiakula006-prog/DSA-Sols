# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def check(node,v):
            if node.val == v:
                return True
            elif v < node.val and node.left:
                return check(node.left,v)
            elif v > node.val and node.right:
                return check(node.right,v)
            return False

        ans = [None]

        def dfs(node):
            if not node:
                return False
            if check(node,p.val) and check(node,q.val):
                if not (dfs(node.left) or dfs(node.right)):
                    ans[-1] = node
                return True
            else:
                return False
        dfs(root)
        return ans[-1]