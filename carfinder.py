# Inheritance
class Vehicle:
    def __init__(self, Make, Model, Year, Mileage, Price):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Mileage = Mileage
        self.Price = Price
        
    def getMake(self):
        return self.Make
    def setMake(self, newMake):
        self.Make = newMake
        
    def getModel(self):
        return self.Model
    def setModel(self, newModel):
        self.Model = newModel
        
    def getYear(self):
        return self.Year
    def setYear(self, newYear):
        self.Year = newYear
        
    def getMileage(self):
        return self.Mileage
    def setMileage(self, newMileage):
        self.Mileage = newMileage
        
    def getPrice(self):
        return self.Price
    def setPrice(self, newPrice):
        self.Price = newPrice

    def Display(self):
        print('Make:  ' + str(self.Make))
        print('Year:  ' + str(self.Year))
        print('Model: ' + str(self.Model))
        print('Miles: ' + str(self.Mileage))
        print('Price: ' + str(self.Price))


class Car(Vehicle):
    def __init__(self, auto, Doors):
        self.Make = auto.getMake()
        self.Model = auto.getModel()
        self.Year = auto.getYear()
        self.Mileage = auto.getMileage()
        self.Price = auto.getPrice()
        self.Doors = Doors

    def getDoors(self):
        return self.Doors
    def setDoors(self, newDoors):
        self.Doors = newDoors

    def Display(self):
        print('Inventory unit: Car')
        super(Car, self).Display()
        print('Number of doors: ' + str(self.Doors))


class Truck(Vehicle):
    def __init__(self, auto, Drive):
        self.Make = auto.getMake()
        self.Model = auto.getModel()
        self.Year = auto.getYear()
        self.Mileage = auto.getMileage()
        self.Price = auto.getPrice()
        self.Drive = Drive

    def getDrive(self):
        return self.Drive
    def setDrive(self, newDrive):
        self.Drive = newDrive

    def Display(self):
        print('Inventory unit: Truck')
        super(Truck, self).Display()
        print('Drive type: ' + str(self.Drive))


class SUV(Vehicle):
    def __init__(self, auto, Capacity):
        self.Make = auto.getMake()
        self.Model = auto.getModel()
        self.Year = auto.getYear()
        self.Mileage = auto.getMileage()
        self.Price = auto.getPrice()
        self.Capacity = Capacity

    def getCapacity(self):
        return self.Capacity
    def setCapacity(self, newCapacity):
        self.Capacity = newCapacity

    def Display(self):
        print('Inventory unit: SUV')
        super(SUV, self).Display()
        print('Passenger Capacity: ' + str(self.Capacity))


class Inventory:
    def __init__(self, ven = []):
        self.ven = ven[:]
    def addVehicle(self, Vehicle):
        self.ven.append(Vehicle)
    def Display(self):
        for Vehicle in self.ven:
            print()
            Vehicle.Display()
            print()



def main():
    test3 = Inventory()
    while True:
        vehicletype = input('Enter a vehicle type (Car, Truck, or SUV), or press ENTER to quit: ')
        if not vehicletype:
            test3.Display()
            return
        vehicletype = vehicletype.upper()
        if vehicletype == 'CAR':
            userMake = input('Enter car\'s make: ')
            userModel = input('Enter car\'s model: ')
            userYear = input('Enter car\'s year: ')
            userMileage = input('Enter car\'s mileage: ')
            userPrice = input('Enter car\'s price: ')
            userAdditional = input('Enter number of doors (2 or 4): ')
        elif vehicletype == 'TRUCK':
            userMake = input('Enter truck\'s make: ')
            userModel = input('Enter truck\'s model: ')
            userYear = input('Enter truck\'s year: ')
            userMileage = input('Enter truck\'s mileage: ')
            userPrice = input('Enter truck\'s price: ')
            userAdditional = input('Enter drive type (2-wheel or 4-wheel drive: ')
        elif vehicletype =='SUV':
            userMake = input('Enter SUV\'s make: ')
            userModel = input('Enter SUV\'s model: ')
            userYear = input('Enter SUV\'s year: ')
            userMileage = input('Enter SUV\'s mileage: ')
            userPrice = input('Enter SUV\'s price: ')
            userAdditional = input('Enter passenger Capacity: ')
            
        test = Vehicle(userMake, userModel, userYear, userMileage, userPrice)
        if vehicletype == 'CAR':
            test2 = Car(test, userAdditional)
        elif vehicletype == 'TRUCK':
            test2 = Truck(test, userAdditional)
        elif vehicletype == 'SUV':
            test2 = SUV(test, userAdditional)
        test3.addVehicle(test2)
