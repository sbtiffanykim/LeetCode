class MedianFinder:

    def __init__(self):
        self.lower = []  # max_heap: stores the lower half of the numbers
        self.upper = []  # min_heap: stores the upper half of the numbers

    def addNum(self, num: int) -> None:
        if self.upper and num > self.upper[0]:
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -1 * num)
        
        # Rebalance the heaps - the size difference between the heaps is at most 1
        if len(self.upper) > len(self.lower) + 1:
            heapq.heappush(self.lower, -1 * heapq.heappop(self.upper))
        if len(self.lower) > len(self.upper) + 1:
            heapq.heappush(self.upper, -1 * heapq.heappop(self.lower))        

    def findMedian(self) -> float:
        if len(self.upper) > len(self.lower):
            return self.upper[0]
        elif len(self.lower) > len(self.upper):
            return -1 * self.lower[0]
        else:
            return (-1 * self.lower[0] + self.upper[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()