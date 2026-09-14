# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        count = 0

        def check(node: TreeNode) -> None:
            nonlocal count
            if node is None:
                return
            if len(stack) == 0 or node.val >= stack[-1]:
                stack.append(node.val)
                count+=1
            else:
                stack.append(stack[-1])
            if node.left: 
                check(node.left)
                stack.pop()
            if node.right: 
                check(node.right)
                stack.pop()
        
        check(root)
        return count