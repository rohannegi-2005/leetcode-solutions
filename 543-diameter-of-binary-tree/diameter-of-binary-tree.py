# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if node is None:
                return 0

            return 1 + max(height(node.left), height(node.right))

        def diameter(node):

            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            curr_diameter = left + right

            return max(curr_diameter, diameter(node.left), diameter(node.right) )


        return diameter(root)





            
        