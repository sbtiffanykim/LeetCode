class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        n, m = len(image), len(image[0])
        
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m:
                return image
            if image[x][y] == target:
                image[x][y] = color
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)
            return image
        
        target = image[sr][sc]
        if target == color:
            return image
        return dfs(sr, sc)