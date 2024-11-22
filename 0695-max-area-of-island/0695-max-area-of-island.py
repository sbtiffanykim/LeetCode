class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        # Returns the area of current island
        def bfs(i: int, j: int) -> int:
            area = 0
            queue = deque()
            queue.append((i, j))
            grid[i][j] = -1  # Mark as visited
            
            while queue:
                x, y = queue.popleft()
                area += 1
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] < 1:  # Out of bound / not an island / already visited
                        continue
                    queue.append((nx, ny))
                    grid[nx][ny] = -1
            
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j))
                    
        return max_area