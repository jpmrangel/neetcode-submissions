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

        def maxDepth(root: Optional[TreeNode]) -> [int, int]:
            if root is None:
                return [0, 0]
            leftH, lDiameter = maxDepth(root.left)
            rightH, rDiameter = maxDepth(root.right)
            maxD = max(lDiameter, rDiameter)
            d = leftH + rightH
            if d > maxD:
                maxD = d
            return [1 + max(leftH, rightH), maxD] 

        depth, diameter = maxDepth(root)

        return diameter
            