# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        node = root
        stack = []
        pre = None
        smallest = None
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:    
                node = stack.pop()
                if not smallest:
                    smallest = node
                node.left = None
                if pre:
                    pre.right = node
                pre = node
                node = node.right
        return smallest
