# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node: Optional[TreeNode]) -> tuple[int, int]:
            if node is None:
                return (0, 0)
            leftH, leftBest = depth(node.left)
            rightH, rightBest = depth(node.right)
            best = max(leftBest, rightBest, leftH + rightH)
            return (1 + max(leftH, rightH), best) 

        _, best = depth(root)

        return best
            