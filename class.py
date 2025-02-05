class car:
    def __init__(self,brand,model,year):#construct
        self.brand=brand#attribute
        self.model=model
        self.year=year
    
    def start(self,time):#method
        print(f'car {self.model} is staring{time}')


car1=car("BMW","X500",2020)
print(f'car {car1.brand} and {car1.model}')
car1.start(10)