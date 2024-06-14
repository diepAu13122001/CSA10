class Counter:
    def __init__(self, name):
        self.count = 0
        self.name = name

    def tick(self):
        self.count += 1
        print(self.name, self.count)

    def reset(self):
        self.count = 0
        print("Reset", self.name)

    def setCount(self, count):
        self.count = count + 1
        return count  # tra ve param


# tao obj
counter1 = Counter(name="1")
counter1.tick()
counter1.reset()  # count => 0

print(counter1.setCount(12))
# counter1.reset()
print(counter1.count)
counter1.count = 1

counter2 = Counter(name="2")
counter2.tick()
counter2.reset()
