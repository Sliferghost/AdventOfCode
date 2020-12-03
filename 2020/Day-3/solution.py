def split(word):
    return [character for character in word]

def readMap():
    map = []
    with open('map') as file:
        for line in file:
            map.append(split(line.strip()))
    return map


map = readMap()
reachedBottom = False
amountOfTrees = 0
startPosition = {
    "x": 0,
    "y": 0
}

while not reachedBottom:
    startPosition['x'] += 3
    startPosition['y'] += 1

    if startPosition['x'] not in range(len(map[0])):
        map = [row + row for row in map]
    if startPosition['y'] not in range(len(map)):
        reachedBottom = True
        break

    characterOnMap = map[startPosition['y']][startPosition['x']]

    if characterOnMap == "#":
        amountOfTrees += 1

print(f"Amount of trees: {amountOfTrees}")