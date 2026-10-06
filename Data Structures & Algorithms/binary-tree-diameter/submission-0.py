# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        mx = 0

        def depth(node):
            nonlocal mx

            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)

            mx = max(left+right,mx)
            return 1 + max(left,right)
        depth(root)
        return mx


                
                

        