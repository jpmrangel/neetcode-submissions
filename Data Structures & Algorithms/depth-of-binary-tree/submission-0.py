# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def depth(root:Optional[TreeNode]) -> int:
            if root.left and root.right:
                return 1 + max(depth(root.left), depth(root.right))
            elif root.left:
                return 1 + depth(root.left)
            elif root.right:
                return 1 + depth(root.right)
            else:
                return 1

        return depth(root)
