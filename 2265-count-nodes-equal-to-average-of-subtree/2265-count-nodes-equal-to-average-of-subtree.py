# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        self.result = 0
        def helper(root):
            if not root:
                return 0,0
            
            sum_left , size_left = helper(root.left)
            sum_right, size_right = helper(root.right)
            
            current_sum = sum_left + sum_right + root.val
            current_size = size_left + size_right + 1
            
            if current_sum // current_size == root.val:
                self.result += 1
                
            return current_sum, current_size
                
        helper(root)
        return self.result