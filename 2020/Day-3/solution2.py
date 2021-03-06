def split(word):
    return [character for character in word]

def readMap():
    map = []
    with open('map') as file:
        for line in file:
            map.append(split(line.strip()))
    return map


def countTreesOnMap(slopeX, slopeY):
    map = readMap()
    reachedBottom = False
    amountOfTrees = 0
    startPosition = {
        "x": 0,
        "y": 0
    }

    while not reachedBottom:
        startPosition['x'] += slopeX
        startPosition['y'] += slopeY

        if startPosition['x'] not in range(len(map[0])):
            map = [row + row for row in map]
        if startPosition['y'] not in range(len(map)):
            reachedBottom = True
            break

        characterOnMap = map[startPosition['y']][startPosition['x']]

        if characterOnMap == "#":
            amountOfTrees += 1

    return amountOfTrees

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]
total = 1

for slope in slopes:
    total *= countTreesOnMap(slope[0], slope[1])

print(f"Solution: {total}")