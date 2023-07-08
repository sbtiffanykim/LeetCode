class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != '1':
                return
            grid[x][y] = '#'
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
        
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
        return cnt