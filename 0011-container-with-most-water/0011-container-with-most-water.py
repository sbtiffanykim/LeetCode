class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        answer = 0  # max area
        while left < right:
            container_h = min(height[left], height[right]) 
            area = container_h * (right - left)
            answer = max(answer, area)  # update the max area
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return answer