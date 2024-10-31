# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Check if the subRoot is the subtree of the root
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:  # If the root is not null but the subRoot is null
            return True
        if not root:  # If the root is null but the subRoot is null
            return False
        if self.isSameTree(root, subRoot):
            return True
        # Search recursively
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    # Check if the two given trees are the same        
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right))
        return False