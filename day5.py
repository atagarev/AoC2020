import math
import re
from functools import total_ordering

from utils import readFile

@total_ordering
class PlaneSeat():


    def __init__(self, s):
        if re.match("^[FB]{7}[LR]{3}$", s) is None:
            raise ValueError("Plane seat specification strin {} is not valid.".format(s))
        self.id = 0
        for l in s:
            if l == "F" or l == "L":
                self.id = 2*self.id
            else:
                self.id = 2*self.id + 1
        self.row = math.floor(self.id/8)
        self.seat = math.remainder(self.id, 8)

    def getId(self):
        return self.id

    def getRow(self):
        return self.row

    def getSeat(self):
        return self.seat

    def __eq__(self, other):
        if isinstance(other, PlaneSeat):
            return self.id == other.id
        return False

    def __lt__(self, other):
        if not isinstance(other, PlaneSeat):
            raise ValueError("Invalid comparison operation!")
        return self.id < other.id

def challenge(lines):
    seats = []
    for line in lines:
        seats.append(PlaneSeat(line.strip()))

    maxId = 0
    for seat in seats:
        if seat.getId() > maxId:
            maxId = seat.getId()
    print("The largest seat id is currently {}.".format(maxId))

    seats.sort()
    for i, s in enumerate(seats):
        if i == 0:
            pass
        elif s.getId() - seats[i-1].getId() > 1:
            print("Missing seats discovered. Its id {}.".format(s.getId()-1))
            break
    print("Got an array with {} seats out of an input file with {} lines.".format(len(seats), len(lines)))

if __name__ == "__main__":
    lines = readFile("data/d5.txt")
    challenge(lines)