class MovingAverage:
    
    def __init__(self, size: int):
        self.size = size
        self.temp = []

    def next(self, val: int) -> float:
        if len(self.temp) == self.size:
            self.temp = self.temp[1:]
        if len(self.temp) < self.size:
            self.temp.append(val)
        return sum(self.temp) / len(self.temp)
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)