# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest = 0  # the longest diameter 
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Returns height
        def dfs(curr):  
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            self.longest = max(self.longest, left + right)  # Keep updating the diameter            
            return 1 + max(left, right)
        
        dfs(root)
        return self.longest
            