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
        raise ValueError("Encountered unknown seat type value: {}".format(v))

class Direction(Enum):
    NW = (-1, -1)
    N = (0, -1)
    NE = (1, -1)
    E = (1, 0)
    SE = (1, 1)
    S = (0, 1)
    SW = (-1, 1)
    W = (-1, 0)

    def getOffsetX(self):
        return self.value[0]

    def getOffsetY(self):
        return self.value[1]

class SeatingPlan():

    def __init__(self, rows):
        m = []
        for row in rows:
            r = []
            for p in row:
                r.append(PlaceType.getTypeByMapsymbol(p))
            m.append(r)
        self.map = m
        self.height = len(m)
        self.width = len(m[0])

    def __eq__(self, other):
        if not isinstance(other, SeatingPlan):
            return False
        if self.height != other.height or self.width != other.width:
            return False
        for x in range(self.width):
            for y in range(self.height):
                if self.getValueAtCoordinates(x, y) != other.getValueAtCoordinates(x, y):
                    return False
        return True

    def validCoordinates(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return False
        return True

    def getValueAtCoordinates(self, x, y):
        if not self.validCoordinates(x, y):
            raise ValueError("Coordinates {}, {} are out of bounds.".format(x, y))
        return self.map[y][x]

    def sumSurroundings(self, x, y):
        sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                xp = x+i
                yp = y+j
                if self.validCoordinates(xp, yp) and not (xp == x and yp == y):
                    if self.getValueAtCoordinates(xp, yp).placeTaken():
                        sum += 1
        return sum

    def countTakenSeats(self):
        taken = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.getValueAtCoordinates(x, y).placeTaken():
                    taken += 1
        return taken

    def doISeeTakenSeat(self, x, y, d):
        xp = x+d.getOffsetX()
        yp = y+d.getOffsetY()
        if xp < 0 or yp < 0 or xp >= self.width or yp >= self.height:
            return 0
        p = self.getValueAtCoordinates(xp, yp)
        if p.placeTaken():
            return 1
        elif p == PlaceType.Floor:
            return self.doISeeTakenSeat(xp, yp, d)
        return 0

    def sumTakenSeatsInSight(self, x, y):
        taken = 0
        for d in Direction:
            taken += self.doISeeTakenSeat(x, y, d)
        return taken

    def buildNextSeatingPlan(self):
        nextSeatingPlan = []
        for y, r in enumerate(self.map):
            nextRow = []
            for x, p in enumerate(r):
                neighbours = self.sumSurroundings(x, y)
                if p == PlaceType.FreeSeat and neighbours == 0:
                    nextRow.append(PlaceType.TakenSeat.value)
                elif p == PlaceType.TakenSeat and neighbours > 3:
                    nextRow.append(PlaceType.FreeSeat.value)
                else:
                    nextRow.append(p.value)
            nextSeatingPlan.append(nextRow)
        return nextSeatingPlan

    def buildNextSeatingPlanv2(self):
        nextSeatingPlan = []
        for y, r in enumerate(self.map):
            nextRow = []
            for x, p in enumerate(r):
                neighbours = self.sumTakenSeatsInSight(x, y)
                if p == PlaceType.FreeSeat and neighbours == 0:
                    nextRow.append(PlaceType.TakenSeat.value)
                elif p == PlaceType.TakenSeat and neighbours > 4:
                    nextRow.append(PlaceType.FreeSeat.value)
                else:
                    nextRow.append(p.value)
            nextSeatingPlan.append(nextRow)
        return nextSeatingPlan

def finalizeSeatingPlanv1(lines):
    pCurr = SeatingPlan(lines)
    print("Initial state has {} taken seats.".format(pCurr.countTakenSeats()))
    pNext = SeatingPlan(pCurr.buildNextSeatingPlan())
    print("First iteration has {} taken seats.".format(pNext.countTakenSeats()))
    i = 0
    while pCurr != pNext:
        pCurr = pNext
        pNext = SeatingPlan(pCurr.buildNextSeatingPlan())
        i += 1
    print("Iteration {} has finally stabilized and has {} taken seats.".format(i, pCurr.countTakenSeats()))

def finalizeSeatingPlanv2(lines):
    pCurr = SeatingPlan(lines)
    print("Initial state has {} taken seats.".format(pCurr.countTakenSeats()))
    pNext = SeatingPlan(pCurr.buildNextSeatingPlanv2())
    print("First iteration has {} taken seats.".format(pNext.countTakenSeats()))
    i = 0
    while pCurr != pNext:
        pCurr = pNext
        pNext = SeatingPlan(pCurr.buildNextSeatingPlanv2())
        i += 1
    print("Iteration {} has finally stabilized and has {} taken seats.".format(i, pCurr.countTakenSeats()))

if __name__ == "__main__":
    lines = readFile("data/d11.txt")
    finalizeSeatingPlanv1(lines)
    print("\n#####\n")
    finalizeSeatingPlanv2(lines)
