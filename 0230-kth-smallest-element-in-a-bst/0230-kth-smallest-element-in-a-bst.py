
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        idx = [0]
        ans = [-1]
        def dfs(n):
            if ans[-1]>=0:
                return
            if n.left:
                dfs(n.left)
            idx[-1]+=1
            if idx[-1]==k:
                ans[-1] = n.val
                return
            if n.right:
                dfs(n.right)

        dfs(root)
        return ans[-1]
