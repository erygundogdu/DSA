# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS
        #if not root:
           # return 0
        #depth_r = self.maxDepth(root.right)
        #depth_l = self.maxDepth(root.left)

       # return max(depth_r,depth_l) +1
        #BFS
        from collections import deque
        if not root:
            return 0
        q = deque()
        q.append(root)
        cnt = 0
        while q:
            cnt +=1
            for _ in range(len(q)):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)    
        return cnt







        