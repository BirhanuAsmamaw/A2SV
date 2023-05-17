# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if (root == None):
            return 0 
        
        result = 0
        if (root.val % 2 == 0):
            if (root.left != None and root.left.left != None):
                result += root.left.left.val
            if (root.left != None and root.left.right != None):
                result += root.left.right.val
            if (root.right != None and root.right.left != None):
                result += root.right.left.val
            if (root.right != None and root.right.right != None):
                result += root.right.right.val
        result += self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)
        return result