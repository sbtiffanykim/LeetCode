class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        # binary search - row
        top, bot = 0, rows - 1
        while top <= bot:
            row = top + (bot - top) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        
        if not(top <= bot): # none of the rows contain the target value
            return False
        row = (top + bot) // 2
            
        # binary search - column
        left, right = 0, cols - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True
        return False