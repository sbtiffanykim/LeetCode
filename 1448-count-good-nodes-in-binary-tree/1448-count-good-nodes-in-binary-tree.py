# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque()
        res = 0
        queue.append((root, -float('inf')))
        
        while queue:
            cur_node, max_val = queue.popleft()
            if cur_node.val >= max_val:
                res += 1
            
            if cur_node.left:
                queue.append((cur_node.left, max(max_val, cur_node.val)))
            if cur_node.right:
                queue.append((cur_node.right, max(max_val, cur_node.val)))                
        
        return res