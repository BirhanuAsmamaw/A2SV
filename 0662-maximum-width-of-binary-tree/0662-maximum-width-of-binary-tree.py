# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append([root,0])
        max_width = 1
        
        while queue:
            left_pointer = queue[0][1]
            right_pointer = queue[-1][1]
            max_width = max(max_width, right_pointer - left_pointer + 1)
        
            for i in range(len(queue)):
                current , index = queue.popleft()
                if current.left:
                    queue.append([current.left , 2*index + 1])
                if current.right:
                    queue.append([current.right , 2*index + 2])
                    
        return max_width