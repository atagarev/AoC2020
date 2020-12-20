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

def buildContainedInMap(rules):
    containedMap = dict()
    for rule in rules:
        for innerBag in rule.getInner():
            containedIn = None
            if containedMap.__contains__(innerBag):
                containedIn = containedMap[innerBag]
            else:
                containedIn = set()
            containedIn.add(rule.getOuter())
            containedMap[innerBag] = containedIn
    return containedMap

def buildInclusiveSet(map, name):
    r = set()
    if map.__contains__(name):
        r = map.get(name)
        for bag in map.get(name):
            r = r.union(buildInclusiveSet(map, bag))
    return r

def findRuleByOuterName(rules, name):
    for rule in rules:
        if rule.getOuter() == name:
            return rule
    raise ValueError("No matching rule found for bag type {}".format(name))

def countDownstream(rules, name):
    r = 1
    rule = findRuleByOuterName(rules, name)
    for inner in rule.getInner():
        mult = int(rule.getInner()[inner])
        r += mult * countDownstream(rules, inner)
    return r

if __name__ == "__main__":
    lines = readFile("data/d7.txt")
    rules = []
    for line in lines:
        rules.append(Rule(line))
    print("Processed total of {} rules.".format(len(rules)))
    upMap = buildContainedInMap(rules)
    bagName = "shiny gold"
    incUpSet = buildInclusiveSet(upMap, bagName)
    print("{} bag can be contained in {} other kinds of bags.".format(bagName, len(incUpSet)))
    cnt = countDownstream(rules, bagName)
    print("{} bag has to contain {} other bags to conform to the rules.".format(bagName, cnt))
    # for bn in inclusionMap:
    #     cnt = len(inclusionMap[bn])
    #     print("{} bag can be contained in {} other kinds of bags.".format(bn, cnt))