# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _dfs(self, node: Optional[TreeNode], path: list, res) -> None:
        # Base Case
        if not node:
            return 
        # Append the current node value to the path
        path.append(str(node.val))
        # If it's a leaf node, add the path to the result        
        if not node.left and not node.right:
            res.append('->'.join(path))
        # Recursive traversal
        self._dfs(node.left, path, res)
        self._dfs(node.right, path, res)
        # Backtracking
        path.pop()
            
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:     
        result = []
        self._dfs(root, [], result)
        return result