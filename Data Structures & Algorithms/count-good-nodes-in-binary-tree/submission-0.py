# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,mx):

            if node is None:
                return 0
            if node.val >= mx:
                good = 1
                mx = max(node.val,mx)
            else:
                good = 0
            return good + dfs(node.left,mx) + dfs(node.right,mx)
        
        return dfs(root,root.val)
             

        