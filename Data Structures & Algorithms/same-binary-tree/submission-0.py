# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def isEqual(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1 and not node2:
                return True
            elif node1 and not node2 or not node1 and node2:
                return False
            l = isEqual(node1.left, node2.left)
            r = isEqual(node1.right, node2.right)
            eq = False
            if node1.val == node2.val:
                eq = True
            
            return eq and l and r
            
        
        return isEqual(p, q)