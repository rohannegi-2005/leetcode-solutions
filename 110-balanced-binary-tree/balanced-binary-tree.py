# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def check_balance(node):

            if node is None:
                return True
            
            left_h = height(node.left)
            right_h = height(node.right)

            if abs(left_h - right_h) > 1:
                return False

            return check_balance(node.left) and check_balance(node.right)


        return check_balance(root)
            
        