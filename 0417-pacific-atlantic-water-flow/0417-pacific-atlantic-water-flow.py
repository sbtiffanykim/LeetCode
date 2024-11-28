class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        rows, cols = len(heights), len(heights[0])
        res = []
        
        # Lists to track which cells can reach the Pacific and Atlantic oceans        
        can_reach_pacific = [[False] * cols for _ in range(rows)]
        can_reach_atlantic = [[False] * cols for _ in range(rows)]        

        # BFS
        def bfs(ocean_reach, start_points):
            q = deque(start_points)
            while q:
                x, y = q.popleft()
                ocean_reach[x][y] = True
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    # Check if the neighbor is within bounds and the height is non-increasing
                    if 0 <= nx < rows and 0 <= ny < cols and heights[nx][ny] >= heights[x][y] and not ocean_reach[nx][ny]:
                        q.append((nx, ny))

        # Initialize the start points for both Pacific and Atlantic                    
        pacific_start = []
        atlantic_start = []
        for r in range(rows):
            pacific_start.append((r, 0))
            atlantic_start.append((r, cols - 1))
        
        for c in range(cols):
            pacific_start.append((0, c))
            atlantic_start.append((rows - 1, c))
        
        # Perform BFS for both oceans
        bfs(can_reach_atlantic, atlantic_start)
        bfs(can_reach_pacific, pacific_start)
        
        for i in range(rows):
            for j in range(cols):
                if can_reach_pacific[i][j] and can_reach_atlantic[i][j]:
                    res.append([i, j])
                    
        return res