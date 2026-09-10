# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isEqual(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1 and not node2:
                return True
            elif node1 and not node2 or not node1 and node2:
                return False
            l, r = isEqual(node1.left, node2.left), isEqual(node1.right, node2.right)
            return l and r and node1.val==node2.val

        def sameTree(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if root1 is None:
                return False
            e = isEqual(root1, root2)
            if e:
                return True
            l = sameTree(root1.left, root2)
            if l:
                return True
            r = sameTree(root1.right, root2)
            if r:
                return True
            return l or r


        return sameTree(root, subRoot)