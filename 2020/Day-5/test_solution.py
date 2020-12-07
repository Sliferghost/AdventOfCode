from solution import seatToId, determineColumn, determineRow

def test_determineColumn_onlyLeft():
    columns = 'LLL'
    assert determineColumn(columns) == 0
def test_determineColumn_onlyRight():
    columns = 'RRR'
    assert determineColumn(columns) == 7
def test_determineColumn_combinations():
    assert determineColumn('LLR') == 1
    assert determineColumn('LRL') == 2
    assert determineColumn('LRR') == 3
    assert determineColumn('RLL') == 4
    assert determineColumn('RLR') == 5
    assert determineColumn('RRL') == 6

def test_determineRow_onlyFront():
    rows = 'FFFFFFF'
    assert determineRow(rows) == 0
def test_determineRow_onlyBack():
    rows = 'BBBBBBB'
    assert determineRow(rows) == 127
def test_determineRow_combinations():
    assert determineRow('FFFBBBF') == 14


def test_seatToId_testCases():
    assert seatToId('FBFBBFFRLR') == 357
    assert seatToId('BFFFBBFRRR') == 567
    assert seatToId('FFFBBBFRRR') == 119
    assert seatToId('BBFFBBFRLL') == 820