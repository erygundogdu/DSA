# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        from collections import deque
        
        def serialize(node):

            results = []
            q = deque()
            q.append(node)
            while q:
                n = q.popleft()
                if n is None:
                    results.append(None)
                    continue
                if n.right:
                    q.append(n.right)
                if n.left:
                    q.append(n.left)
                results.append(n.val)
            return results
        tgt = serialize(subRoot)
        q1 = deque()

        q1.append(root)
        while q1:
            node1 = q1.popleft()
            if serialize(node1) == tgt:
                return True
            if node1.right:
                q1.append(node1.right)
            if node1.left:
                q1.append(node1.left)
        return False



        


        
        
        