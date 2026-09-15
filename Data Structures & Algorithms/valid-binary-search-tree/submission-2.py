# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, interval) -> bool:
            if node is None:
                return True
            return node.val>interval[0] and node.val<interval[1] and check(node.left, [interval[0], node.val]) and check(node.right, [node.val, interval[1]])
        return check(root, [float('-inf'), float('inf')])