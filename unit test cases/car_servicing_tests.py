import unittest
from components import CarServicing, CarType, Engine, Battery, Tire, ServiceCriteria, Car

class CarServicingTests(unittest.TestCase):
    def setUp(self):
        # Create car servicing instance
        self.carServicing = CarServicing()

        # Create car types
        self.capuletEngine = Engine("Capulet Engine")
        self.willoughbyEngine = Engine("Willoughby Engine")
        self.sternmanEngine = Engine("Sternman Engine")
        self.spindlerBattery = Battery("Spindler Battery")
        self.nubbinBattery = Battery("Nubbin Battery")
        self.spindlerTire = Tire("Spindler Tire")

        # Create car models and associate with car types
        self.calliope = CarType("Calliope", self.capuletEngine, self.spindlerBattery, self.spindlerTire)
        self.glissade = CarType("Glissade", self.willoughbyEngine, self.spindlerBattery, self.spindlerTire)
        self.palindrome = CarType("Palindrome", self.sternmanEngine, self.spindlerBattery, self.spindlerTire)
        self.rorschach = CarType("Rorschach", self.willoughbyEngine, self.nubbinBattery, self.spindlerTire)
        self.thovex = CarType("Thovex", self.capuletEngine, self.nubbinBattery, self.spindlerTire)

        # Add car types to the car servicing system
        self.carServicing.addServiceCriteria(self.calliope, ServiceCriteria(30000))
        self.carServicing.addServiceCriteria(self.glissade, ServiceCriteria(60000))
        self.carServicing.addServiceCriteria(self.palindrome, ServiceCriteria(0))
        self.carServicing.addServiceCriteria(self.rorschach, ServiceCriteria(0))
        self.carServicing.addServiceCriteria(self.thovex, ServiceCriteria(0))

    def test_carServicingNotRequired(self):
        # Create a car instance with mileage below the threshold
        car = Car(self.calliope, mileage=25000)

        # Check if car servicing is required
        result = self.carServicing.isServiceRequired(car)

        # Assert that car servicing is not required
        self.assertFalse(result)

    def test_carServicingRequired(self):
        # Create a car instance with mileage above the threshold
        car = Car(self.calliope, mileage=35000)

        # Check if car servicing is required
        result = self.carServicing.isServiceRequired(car)

        # Assert that car servicing is required
        self.assertTrue(result)

    def test_getServiceCriteria(self):
        # Get service criteria for a specific car type
        criteria = self.carServicing.getServiceCriteria(self.glissade)

        # Assert that the correct service criteria is returned
        self.assertEqual(criteria.getMileageThreshold(), 60000)


if __name__ == '__main__':
    unittest.main()
