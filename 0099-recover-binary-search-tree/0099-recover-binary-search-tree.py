# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        inorder = []
        def collect(node):
            if not node:
                return 
            collect(node.left)
            inorder.append(node.val)
            collect(node.right)

        collect(root)
        inorder.sort()
        i = [0]
        def do(node):
            if not node:
                return 
            do(node.left)
            node.val = inorder[i[0]]
            i[0] += 1
            do(node.right)
        do(root)