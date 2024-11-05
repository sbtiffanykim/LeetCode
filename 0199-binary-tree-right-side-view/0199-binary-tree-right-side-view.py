# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])
        
        while queue:
            nodes = len(queue)  # number of nodes at the current level
            right = None  # current right node
            for _ in range(nodes):
                cur_node = queue.popleft()
                if cur_node:
                    right = cur_node
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)
            if right:
                res.append(right.val)
                    
        
        return res
        