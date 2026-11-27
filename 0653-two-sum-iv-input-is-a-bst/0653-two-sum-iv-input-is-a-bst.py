# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        s = set()
        def check(node):
            if not node:
                return     
            s.add(k-node.val)
            check(node.left)
            check(node.right)
            return
            
        def search(node):
            if not node:
                return False
            if node.val in s and node.val*2 != k:
                return True
            else:
                return search(node.left) or search(node.right)    

        check(root)     
        return search(root)    