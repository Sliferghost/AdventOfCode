import math

def calculateFuelNeeds(mass: int):
    return math.floor(mass / 3) - 2

sumMass = 0

with open('input.txt') as file:
    for mass in file:
        fuelNeedsForMass = calculateFuelNeeds(int(mass))
        while fuelNeedsForMass > 0:
            sumMass += fuelNeedsForMass
            fuelNeedsForMass = calculateFuelNeeds(fuelNeedsForMass)

print(sumMass)