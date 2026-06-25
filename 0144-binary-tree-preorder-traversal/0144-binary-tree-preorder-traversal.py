# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        ans = []
        '''def dfs(cur):
            if cur:
                ans.append(cur.val)    
                dfs(cur.left)
                dfs(cur.right)
        dfs(root)
        return ans'''
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            if not cur:
                continue
            ans.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)
        return ans