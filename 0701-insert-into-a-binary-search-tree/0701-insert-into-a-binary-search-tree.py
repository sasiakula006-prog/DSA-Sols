# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        n = root
        a = TreeNode(val)
        while n:
            if val<n.val:
                if n.left:
                    n = n.left
                else:
                    n.left = a
                    break
            else:
                if n.right:
                    n = n.right
                else:
                    n.right = a
                    break
        if root:
            return root
        return a
                