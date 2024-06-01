# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root and root.val == key:
            right = root.right
            if right:
                while right.left:
                    right = right.left
                right.left = root.left
                return root.right
            else:
                return root.left
                
        elif root and root.val < key and root.right:
            root.right = self.deleteNode(root.right, key)
        elif root and root.val > key and root.left:
            root.left = self.deleteNode(root.left, key)
        return root
