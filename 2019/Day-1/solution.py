import math

def calculateFuelNeeds(mass: int):
    return math.floor(mass / 3) - 2

sumMass = 0

with open('input.txt') as file:
    for line in file:
        sumMass += calculateFuelNeeds(int(line))

print(sumMass)