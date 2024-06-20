# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = deque()
        queue.append((original,cloned))

        while queue:
            origion, clone = queue.popleft()
            if origion == target:
                return clone
            if origion.left:
                queue.append((origion.left,clone.left))
            if origion.right:
                queue.append((origion.right,clone.right))
        
