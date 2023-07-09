class CarServicing:
    def __init__(self):
        self.criteriaMap = {}

    def addServiceCriteria(self, carType, criteria):
        self.criteriaMap[carType] = criteria

    def removeServiceCriteria(self, carType):
        if carType in self.criteriaMap:
            del self.criteriaMap[carType]

    def getServiceCriteria(self, carType):
        return self.criteriaMap.get(carType)

    def isServiceRequired(self, car):
        carType = car.getCarType()
        criteria = self.criteriaMap.get(carType)
        if criteria is not None:
            return car.getMileage() >= criteria.getMileageThreshold()
        return False


class CarType:
    def __init__(self, name, engine, battery, tire):
        self.name = name
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def getName(self):
        return self.name

    def getEngine(self):
        return self.engine

    def getBattery(self):
        return self.battery

    def getTire(self):
        return self.tire


class Engine:
    def __init__(self, engineType):
        self.type = engineType

    def getType(self):
        return self.type


class Battery:
    def __init__(self, batteryType):
        self.type = batteryType

    def getType(self):
        return self.type


class Tire:
    def __init__(self, tireType):
        self.type = tireType

    def getType(self):
        return self.type


class ServiceCriteria:
    def __init__(self, mileageThreshold):
        self.mileageThreshold = mileageThreshold

    def getMileageThreshold(self):
        return self.mileageThreshold


class Car:
    def __init__(self, carType, mileage):
        self.carType = carType
        self.mileage = mileage

    def getCarType(self):
        return self.carType

    def getMileage(self):
        return self.mileage


# Create car servicing instance
carServicing = CarServicing()

# Create car types
capuletEngine = Engine("Capulet Engine")
willoughbyEngine = Engine("Willoughby Engine")
sternmanEngine = Engine("Sternman Engine")
spindlerBattery = Battery("Spindler Battery")
nubbinBattery = Battery("Nubbin Battery")
spindlerTire = Tire("Spindler Tire")

# Create car models and associate with car types
calliope = CarType("Calliope", capuletEngine, spindlerBattery, spindlerTire)
glissade = CarType("Glissade", willoughbyEngine, spindlerBattery, spindlerTire)
palindrome = CarType("Palindrome", sternmanEngine, spindlerBattery, spindlerTire)
rorschach = CarType("Rorschach", willoughbyEngine, nubbinBattery, spindlerTire)
thovex = CarType("Thovex", capuletEngine, nubbinBattery, spindlerTire)

# Add car types to the car servicing system
carServicing.addServiceCriteria(calliope, ServiceCriteria(30000))
carServicing.addServiceCriteria(glissade, ServiceCriteria(60000))
carServicing.addServiceCriteria(palindrome, ServiceCriteria(0))
carServicing.addServiceCriteria(rorschach, ServiceCriteria(0))
carServicing.addServiceCriteria(thovex, ServiceCriteria(0))

# Example usage
car = Car(calliope, mileage=30000)
if carServicing.isServiceRequired(car):
    print("Car servicing required.")
else:
    print("Car servicing not required.")
