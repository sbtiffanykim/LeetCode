class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def dfs(x: int, y: int, depth: int) -> bool:
            if depth == len(word): 
                return True
            
            # Out of bound or does not match 
            if (x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != word[depth]):
                return False
            
            # Mark as visited
            temp = board[x][y]
            board[x][y] = '#'
            
            # Explore all possible directions
            for k in range(4):
                if dfs(x + dx[k], y + dy[k], depth + 1):
                    return True
            
            # Backtracking: restore the cell's original value
            board[x][y] = temp
            return False
            
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    if dfs(x, y, 0):
                        return True
        return False