# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def subtreesBalanced(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            nonlocal isBalanced
            leftH, rightH = subtreesBalanced(node.left), subtreesBalanced(node.right)

            if abs(leftH - rightH) > 1:
                isBalanced = False
            return 1 + max(leftH, rightH)

        subtreesBalanced(root)
        return isBalanced