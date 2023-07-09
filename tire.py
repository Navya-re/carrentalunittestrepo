from datetime import datetime, timedelta
from components import Tire
import unittest

# Define the Tire class
class Tire:
    def __init__(self, tire_type, installation_date):
        self.type = tire_type
        self.installation_date = installation_date

    def get_type(self):
        return self.type

    def get_installation_date(self):
        return self.installation_date

    def get_age(self):
        today = datetime.now()
        age = today - self.installation_date
        return age.days

# Define the Car class
class Car:
    def __init__(self, car_type, mileage, tire):
        self.car_type = car_type
        self.mileage = mileage
        self.tire = tire

    def get_car_type(self):
        return self.car_type

    def get_mileage(self):
        return self.mileage

    def get_tire(self):
        return self.tire

# Define the CarType class
class CarType:
    def __init__(self, name, engine, battery, tire):
        self.name = name
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def get_name(self):
        return self.name

    def get_engine(self):
        return self.engine

    def get_battery(self):
        return self.battery

    def get_tire(self):
        return self.tire

# Define the Engine class
class Engine:
    def __init__(self, engine_type):
        self.type = engine_type

    def get_type(self):
        return self.type

# Define the Battery class
class Battery:
    def __init__(self, battery_type):
        self.type = battery_type

    def get_type(self):
        return self.type

# Define the CarServicing class
class CarServicing:
    def __init__(self):
        self.criteria_map = {}

    def add_service_criteria(self, car_type, criteria):
        self.criteria_map[car_type] = criteria

    def remove_service_criteria(self, car_type):
        if car_type in self.criteria_map:
            del self.criteria_map[car_type]

    def get_service_criteria(self, car_type):
        return self.criteria_map.get(car_type)

    def is_service_required(self, car):
        car_type = car.get_car_type()
        criteria = self.criteria_map.get(car_type)
        if criteria is not None:
            return (
                car.get_mileage() >= criteria.get_mileage_threshold()
                or car.get_tire().get_age() >= criteria.get_tire_age_threshold()
            )
        return False

# Define the ServiceCriteria class
class ServiceCriteria:
    def __init__(self, mileage_threshold, tire_age_threshold):
        self.mileage_threshold = mileage_threshold
        self.tire_age_threshold = tire_age_threshold

    def get_mileage_threshold(self):
        return self.mileage_threshold

    def get_tire_age_threshold(self):
        return self.tire_age_threshold

# Define the test cases
class CarServicingTests(unittest.TestCase):
    def test_tire_replacement_required(self):
        # Create a car with a tire older than 5 years
        tire_installation_date = datetime.now() - timedelta(days=2000)  # Tire age: 5 years and 2000 days
        tire = Tire("Spindler Tire", tire_installation_date)
        car_type = CarType("Calliope", Engine("Capulet Engine"), Battery("Spindler Battery"), tire)
        car = Car(car_type, mileage=10000, tire=tire)
        service_criteria = ServiceCriteria(30000, 1825)  # Mileage threshold: 30000, Tire age threshold: 1825 (5 years)

        # Add service criteria to the car servicing system
        car_servicing = CarServicing()
        car_servicing.add_service_criteria(car_type, service_criteria)

        # The tire should require replacement
        self.assertTrue(car_servicing.is_service_required(car))

    def test_tire_replacement_not_required(self):
        # Create a car with a tire younger than 5 years
        tire_installation_date = datetime.now() - timedelta(days=1000)  # Tire age: 2 years and 1000 days
        tire = Tire("Spindler Tire", tire_installation_date)
        car_type = CarType("Glissade", Engine("Willoughby Engine"), Battery("Spindler Battery"), tire)
        car = Car(car_type, mileage=5000, tire=tire)
        service_criteria = ServiceCriteria(60000, 1825)  # Mileage threshold: 60000, Tire age threshold: 1825 (5 years)

        # Add service criteria to the car servicing system
        car_servicing = CarServicing()
        car_servicing.add_service_criteria(car_type, service_criteria)

        # The tire should not require replacement
        self.assertFalse(car_servicing.is_service_required(car))

# Run the test cases
if __name__ == "__main__":
    unittest.main()
