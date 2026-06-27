# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        if not root:
            return
        preo = []
        s = []
        s.append(root)
        while s:
            n = s.pop()
            if not n:
                continue
            preo.append(n)
            s.append(n.right)
            s.append(n.left)
        for i in range(len(preo)-1):
            preo[i].left = None
            preo[i].right = preo[i+1]
        preo[-1].left = None
        preo[-1].right = None
        return preo[0]

        