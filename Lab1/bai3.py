from datetime import datetime

class MyDate:
    def __init__(self) -> None:
        self.time = datetime.now() 
    
    def getDate(self):
        way1 = self.time.strftime('%d/%m/%Y')
        way2 = f"{self.time.day:02d}/{self.time.month:02d}/{self.time.year:04d}"
        return way2

    def getTime(self):
        way1 = self.time.strftime('%H:%M:%S')
        way2 = f"{self.time.hour:02d}/{self.time.minute:02d}/{self.time.second:02d}"
        return way1

# create object 
now = MyDate()
print(now.getDate())
print(now.getTime())