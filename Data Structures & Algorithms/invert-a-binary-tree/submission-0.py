# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        return self.invertChildren(root)


    def invertChildren(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left:
            self.invertChildren(root.left)
        if root.right:
            self.invertChildren(root.right)
        aux = root.right
        root.right = root.left
        root.left = aux
        return root