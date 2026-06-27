# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lh(self,n):
        cnt = 0
        while n:
            cnt +=1
            n = n.left
        return cnt
    def rh(self,n):
        cnt = 0
        while n:
            cnt +=1
            n = n.right
        return cnt
    def countNodes(self, root):
        if not root:
            return 0
        l = self.lh(root)
        r = self.rh(root)
        if l == r:
            return 2**(l)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
