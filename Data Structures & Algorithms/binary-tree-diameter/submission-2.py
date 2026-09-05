# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def depth(node: Optional[TreeNode]) -> int:
            nonlocal best
            if node is None:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            best = max(best, l + r)
            return 1 + max(l, r) 

        depth(root)

        return best
            