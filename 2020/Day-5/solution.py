from math import floor, ceil

def split(input: range):
    halfwayPoint = (input.stop - input.start) / 2
    lowerRange = range(input.start, floor(input.start + halfwayPoint))
    higherRange = range(ceil(input.stop - halfwayPoint), input.stop)
    return lowerRange, higherRange

columns = range(7)
def determineColumn(columnCharacters):
    lowerRange, higherRange = split(columns)
    
    for character in columnCharacters:
        if character == 'R':
            lowerRange, higherRange = split(higherRange)
        else:
            lowerRange, higherRange = split(lowerRange)

    return lowerRange.stop

rows = range(127)
def determineRow(rowCharacters):
    lowerRange, higherRange = split(rows)

    for character in rowCharacters:
        if character == 'B':
            lowerRange, higherRange = split(higherRange)
        else:
            lowerRange, higherRange = split(lowerRange)

    return lowerRange.stop

def seatToId(seat):
    rowCharacters = seat[0:7]
    columnCharacters = seat[7:10]

    row = determineRow(rowCharacters)
    column = determineColumn(columnCharacters)

    print(f"Row: {row}, column: {column}")

    return row * 8 + column

currentHighestId = 0
with open('boarding-passes') as file:
    for seat in file:
        seatId = seatToId(seat)
        
        if seatId > currentHighestId:
            currentHighestId = seatId
    print(f"Highest seat ID: {currentHighestId}")