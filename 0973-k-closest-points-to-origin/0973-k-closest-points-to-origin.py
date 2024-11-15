class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res, cal = [], []
        
        for x, y in points:
            distance = (x ** 2) + (y ** 2)  # Calculate the distance
            cal.append((distance, [x, y]))  # Add to the heap
        heapq.heapify(cal)
        
        for _ in range(k):
            _, coord = heapq.heappop(cal)
            res.append(coord)
        
        return res