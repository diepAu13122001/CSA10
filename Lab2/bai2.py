class MathList:
    def __init__(self, values) -> None:
        self.values = values
        self.length = len(values)


    def __str__(self) -> str:
        return str(self.values)
    
    def __add__ (self, num):
        for i in range(len(self.values)):
            self.values[i] += num
        return self
    
    def __sub__ (self, num):
        for i in range(len(self.values)):
            self.values[i] -= num
        # [self.values[i] for i in range(len(self.values))]
        return self
    
list_a = MathList([1,2,3])
print(list_a)
list_a += 2
print(list_a)