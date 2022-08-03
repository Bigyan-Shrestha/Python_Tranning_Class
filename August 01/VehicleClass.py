
class Vehicle:

    def __init__(self, color, brand, vehicleType, noOfWheels, price):
        self.color = color
        self.brand = brand
        self.vehicleType = vehicleType
        self.noOfWheels = noOfWheels
        self.price = price

    def vehicleData(self):
        print('The Color Of Vehicle is '+self.color)
        print('The Brand Of Vehicle is '+self.brand)
        print('The Type Of Vehicle is '+self.vehicleType)
        print('Th Price Of Vehicle is '+self.noOfWheels)
        print('Th Price Of Vehicle is '+self.price)
        
car = Vehicle('Red','Porsche','Car','4','$20k')
bike = Vehicle('Black','Harley Davidson','Bike','4','$15k')
truck = Vehicle('Red','Porsche','Car','4','$50k')

print('__CAR___')
car.vehicleData()

print()
print('__Bike___')
bike.vehicleData()

print()
print('__Truck___')
truck.vehicleData()
