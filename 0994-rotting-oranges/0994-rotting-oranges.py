class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        q = deque()  # (x, y, time)
        time = 0
        fresh = 0
        
        def bfs():
            nonlocal time, fresh
            while q:
                x, y, t = q.popleft()
                time = t
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    # If out of bounds, or not a fresh orange
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    fresh -= 1
                    q.append((nx, ny, t + 1))
                    
        for i in range(rows):
            for j in range(cols):
                # Count fresh oranges
                if grid[i][j] == 1:
                    fresh += 1
                # Add rotten oranges to the queue                
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                
        bfs()
        
        return -1 if fresh != 0 else time