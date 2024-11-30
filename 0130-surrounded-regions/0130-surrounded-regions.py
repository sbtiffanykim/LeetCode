class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        rows, cols = len(board), len(board[0])
        
        # Mark all connected 'O' cells
        def bfs(i, j):
            q = deque()
            q.append((i, j))
            board[i][j] = 'R'
            
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                        continue
                    if board[nx][ny] == 'O':
                        board[nx][ny] = 'R'
                        q.append((nx, ny))

                        
        # 1. Find 'O's on the borders and process them using BFS                        
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and board[i][j] == 'O':
                    bfs(i, j)
        
        for i in range(rows):
            for j in range(cols):
                # 2. Change all unmarked 'O's to 'X'
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                # 3. Change all marked 'S's back to 'O'                    
                elif board[i][j] == 'R':
                    board[i][j] = 'O'
                    
        return board 