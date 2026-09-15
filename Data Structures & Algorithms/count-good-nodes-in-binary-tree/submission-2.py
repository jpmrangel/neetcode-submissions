# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def check(node: TreeNode, max_so_far: int) -> int:
            if node is None:
                return 0
            good = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            return good + check(node.left, new_max) + check(node.right, new_max)
        
        return check(root, float('-inf'))