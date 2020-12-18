from utils import readFile
from enum import Enum

class MapCoordType(Enum):
    FREE = '.'
    TREE = '#'

    def getCoordTypeByValue(v):
        for type in MapCoordType:
            if type.value == v:
                return type
        raise ValueError("Unknown coordinate type encountered " + str(v))

class Map():

    def __init__(self):
        self.map = []

    def addRow(self):
        self.map.append([])

    def addCoordinateTypeToRow(self, y, type):
        if y >= len(self.map):
            raise ValueError("Trying to get values for y-value that is too high.")
        self.map[y].append(type)

    def getCoordType(self, x, y):
        if y >= len(self.map):
            raise ValueError("Trying to get values for y-value that is too high.")
        xMod = x % len(self.map[y])
        return self.map[y][xMod]

    def getMapHeight(self):
        return len(self.map)

class Slope():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Slope with x = " + str(self.x) + " and y = " + str(self.y)

def createMap(lines):
    map = Map()
    for y, line in enumerate(lines):
        map.addRow()
        for coord in line:
            map.addCoordinateTypeToRow(y, MapCoordType.getCoordTypeByValue(coord))
    return map

def challenge(map, slope):
    if not isinstance(slope, Slope):
        raise ValueError("Invalid input provided when slope was expected.")
    x = 0
    y = 0
    trees = 0
    while y < map.getMapHeight():
        if map.getCoordType(x, y) == MapCoordType.TREE:
            trees += 1
        x += slope.x
        y += slope.y
    return trees

lines = readFile("data/d3.txt")
map = createMap(lines)
challenge(map, Slope(3, 1))

slopes = [Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]
multTotal = 1
for slope in slopes:
    count = challenge(map, slope)
    multTotal *= count
    print("Encountered " + str(count) + " trees for slope " + str(slope))

print("Final result " + str(multTotal))