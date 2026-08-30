# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
            
        node = deque([root])
        count = 0

        while node:
            count = count + 1
            curr_level = len(node)
            
            for _ in range(curr_level):

                curr = node.popleft()
    
                if curr.left:
                    node.append(curr.left)
                if curr.right:
                    node.append(curr.right)


        return count
        
        