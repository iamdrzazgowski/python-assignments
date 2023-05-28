class Test:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def multiply(self):
        return self.x * self.y
    def setX(self, x):
        self.x = x
    

p1 = Test(5,6);
print(p1.multiply())
p1.setX(10)
print(p1.multiply())