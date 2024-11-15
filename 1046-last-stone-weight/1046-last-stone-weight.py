class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = list()
        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) >= 2:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, (y - x))
        
        if heap:
            return -heap[0]
        return 0