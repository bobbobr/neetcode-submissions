# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def print_tree(self, root):
        if root is None:
            return

        self.print_tree(root.left)
        self.print_tree(root.right)
        print(root.val)
    
    def change_tree(self, root):
        if root is None:
            return
        store_value = root.left
        root.left = root.right
        root.right = store_value

        self.change_tree(root.left)
        self.change_tree(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.print_tree(root)
        self.change_tree(root)
        return root