# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxD = 0

        def maxDepth(root: Optional[TreeNode]) -> int:
            nonlocal maxD
            if root is None:
                return 0
            leftH = maxDepth(root.left)
            rightH = maxDepth(root.right)
            d = leftH + rightH
            if d > maxD:
                maxD = d
            return 1 + max(leftH, rightH)

        maxDepth(root)

        return maxD
            