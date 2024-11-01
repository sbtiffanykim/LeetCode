# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = collections.defaultdict(list)
        queue = collections.deque([(0, root)])
        
        while queue:
            cur_level, cur_node = queue.popleft()
            res[cur_level].append(cur_node.val)
            if cur_node.left:
                queue.append((cur_level + 1, cur_node.left))
            if cur_node.right:
                queue.append((cur_level + 1, cur_node.right))
        
        return list(res.values())