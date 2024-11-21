class MedianFinder:

    def __init__(self):
        self.length = 0
        self.nums = []

    def addNum(self, num: int) -> None:
        self.length += 1
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        if self.length % 2 == 0:
            idx = self.length // 2
            return (self.nums[idx] + self.nums[idx - 1]) / 2
        else:
            return self.nums[self.length // 2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()