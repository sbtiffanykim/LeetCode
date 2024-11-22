class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            grid[i][j] = '-1'
            
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= row or ny < 0 or ny >= col or grid[nx][ny] != '1':
                        continue
                    queue.append((nx, ny))
                    grid[nx][ny] = '-1'
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    bfs(i, j)
                    res += 1
        
        return res