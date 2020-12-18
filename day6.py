import re

from utils import readFile


class PassengerGroup():

    def __init__(self):
        self.questions = None

    def isPersonValid(s):
        if re.match("^\w*$", s) is None:
            raise ValueError("Invalid person entry {} encountered.".format(s))
        return True

    def countYeses(self):
        return len(self.questions)

class PassengerGroupAny(PassengerGroup):

    def addPerson(self, s):
        PassengerGroup.isPersonValid(s)
        if self.questions is None:
            self.questions = set()
        for c in s:
            self.questions.add(c)


class PassengerGroupAll(PassengerGroup):

    def addPerson(self, s):
        PassengerGroup.isPersonValid(s)
        answers = set()
        for c in s:
            answers.add(c)
        if self.questions is None:
            self.questions = answers
        else:
            self.questions = self.questions.intersection(answers)


def challenge(lines):
    groupsAny = []
    groupsAll = []
    gAny = PassengerGroupAny()
    gAll = PassengerGroupAll()
    totalsAny = 0
    totalsAll = 0
    for line in lines:
        if line.strip() == "":
            groupsAny.append(gAny)
            totalsAny += gAny.countYeses()
            gAny = PassengerGroupAny()
            groupsAll.append(gAll)
            totalsAll += gAll.countYeses()
            gAll = PassengerGroupAll()
        else:
            gAny.addPerson(line.strip())
            gAll.addPerson(line.strip())
    groupsAny.append(gAny)
    totalsAny += gAny.countYeses()
    groupsAll.append(gAll)
    totalsAll += gAll.countYeses()
    return totalsAny, groupsAny, totalsAll, groupsAll


if __name__ == "__main__":
    lines = readFile("d6.txt")
    totalsAny, groupsAny, totalsAll, groupsAll  = challenge(lines)
    print("Total number of yeses counted the first way is {}.".format(totalsAny))
    print("Total nuber of yeses counted the second way is {}.".format(totalsAll))
