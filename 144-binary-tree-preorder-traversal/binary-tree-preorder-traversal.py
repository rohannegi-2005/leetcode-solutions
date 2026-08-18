# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def preorder(root, arr):
            if root is None:
                return 
            arr.append(root.val)
            preorder(root.left, arr)
            preorder(root.right, arr)

        arr = []

        preorder(root, arr)

        return arr


        