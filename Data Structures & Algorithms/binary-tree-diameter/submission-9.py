# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        def depth(node):
            nonlocal best
            if node is None:
                return 0
            leftH = depth(node.left)
            rightH = depth(node.right)
            best = max(best, leftH + rightH)
            return 1 + max(leftH, rightH)

        depth(root)

        return best
            