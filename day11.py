from enum import Enum

from utils import readFile

class PlaceType(Enum):
    FreeSeat = "L"
    TakenSeat = "#"
    Floor = "."

    def placeTaken(self):
        return self == PlaceType.TakenSeat

    def getTypeByMapsymbol(v):
        for t in PlaceType:
            if t.value == v:
                return t
        return None

class SeatingPlan():

    def __init__(self, rows):
        m = []
        for y, row in enumerate(rows):
            r = []
            for x, p in enumerate(row):
                r.append(PlaceType.getTypeByMapsymbol(p))
            m.append(r)
        self.map = m
        self.height = len(m)
        self.width = len(m[0])

    def validCoordinates(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return False
        return True

    def getValueAtCoordinates(self, x, y):
        if not self.validCoordinates(x, y):
            raise ValueError("Coordinates {}, {} are out of bounds.".format(x, y))
        seat = self.map[y][x]

    def sumSurroundings(self, x, y):
        sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                xp = x+i
                yp = y+i
                if self.validCoordinates(xp, yp) and not (xp == x and yp == y):
                    if self.getValueAtCoordinates(xp, yp) == PlaceType.TakenSeat:
                        sum += 1
        return sum

    def buildNextStep(self):
        nextPlan = []



if __name__ == "__main__":
    lines = readFile("data/d10.txt")