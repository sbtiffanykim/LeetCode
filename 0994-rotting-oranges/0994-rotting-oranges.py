class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited = [[0] * cols for _ in range(rows)]
        q = deque()  # (x, y, time)
        res = 0
        
        def bfs():
            nonlocal res
            while q:
                x, y, t = q.popleft()
                res = t
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    # If out of bounds, already visited, or not a fresh orange
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or visited[nx][ny] or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    visited[nx][ny] = 1
                    q.append((nx, ny , t + 1))
                    
        # Add rotten oranges to the queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited[i][j] = 1
        
        bfs()
        
        # If there are still fresh oranges left, return -1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
                
        return res