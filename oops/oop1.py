class Cars:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def start(self):
        print(self.name + "Engine Started")


car1 = Cars("Maruti swift", 10000, 'Red')
car2=Cars("Toyota Innova",200000,"White")
print(car1.name)
print(car2.name)
car1.start()
car2.start()