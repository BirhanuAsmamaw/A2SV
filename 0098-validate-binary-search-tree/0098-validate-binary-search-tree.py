# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node,left,right):
            if not node:
                return True
            if not(node.val > left and node.val < right):
                return False
            return  (validate(node.left,left,node.val) and validate(node.right,node.val,right))
        return validate(root,-inf,inf)
            
