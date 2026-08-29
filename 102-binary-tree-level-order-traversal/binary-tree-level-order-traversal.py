# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        ans = []
        node = deque([root])

        while node:
            number = len(node)
            curr_level = []

            for _ in range(number):
                curr = node.popleft()
                curr_level.append(curr.val)

                if curr.left:
                    node.append(curr.left)

                if curr.right:
                    node.append(curr.right)

            ans.append(curr_level)


        return ans
        