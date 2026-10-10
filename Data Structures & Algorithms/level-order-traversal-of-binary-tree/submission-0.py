# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        q = deque()
        if not root:
            return []
        q.append(root)
        res_lst = []
        while q:
            lst = []
            level = len(q)
            for _ in range(level):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                lst.append(node.val)
            res_lst.append(lst)
        return res_lst
            

            

            