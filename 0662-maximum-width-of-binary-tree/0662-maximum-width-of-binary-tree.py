# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        q = deque([(root,1)])
        ans = 0
        while q:
            _,mini = q[0]
            maxi = mini 
            for _ in range(len(q)):
                n,i = q.popleft()
                maxi = i
                if n.left:
                    q.append((n.left,2*i))
                if n.right:
                    q.append((n.right,2*i+1))
                ans = max(ans,maxi-mini+1)
        return ans
