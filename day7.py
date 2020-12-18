import re

from utils import readFile

class Rule():

    def __init__(self, text):
        lhs, rhs = text.split(" bags contain ")
        self.outer = lhs
        self.inner = dict()
        for bag in rhs.split(", "):
            if bag == "no other bags.":
                break
            m = re.match("^(\d+) ([\w ]+) bag", bag)
            if m is None:
                raise ValueError("Invalid inner bag description: {}".format(bag))
            num = m.group(1)
            type = m.group(2)
            self.inner[type] = num

    def getOuter(self):
        return self.outer

    def getInner(self):
        return self.inner

def challenge(rules):
    solutions = set()

if __name__ == "__main__":
    lines = readFile("data/d7.txt")
    rules = []
    for line in lines:
        rules.append(Rule(line))
    print("Processed total of {} rules.".format(len(rules)))
    c1Cnt = challenge(rules)