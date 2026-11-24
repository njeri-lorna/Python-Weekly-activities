
# Parent class
class Vehicle:

    def calculateFare(self, distance):
        pass


# Bus class
class Bus(Vehicle):

    def calculateFare(self, distance):
        return distance * 50


# Taxi class
class Taxi(Vehicle):

    def calculateFare(self, distance):
        return distance * 100


# Main program
bus1 = Bus()
taxi1 = Taxi()

distance = 10

print("Bus Fare:", bus1.calculateFare(distance))
print("Taxi Fare:", taxi1.calculateFare(distance))
