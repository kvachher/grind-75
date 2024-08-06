class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = [] 

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heappush(self.large, -heappop(self.small))
        
        if len(self.small) > len(self.large) + 1:
            heappush(self.large, -heappop(self.small))
        
        if len(self.large) > len(self.small):
            heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
