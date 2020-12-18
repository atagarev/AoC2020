import re

def readFile(filename):
    entries = []
    with open(filename, encoding="utf-8") as f:
        for l in f:
            entries.append(l.strip())
    return entries

def isValidPassword(s):
    cond, pwd = s.split(":")
    m = re.match("^(\d+)-(\d+) (\w)", cond)
    numMin = int(m.group(1))
    numMax = int(m.group(2))
    letter = m.group(3)
    cnt = pwd.count(letter)
    if numMin <= cnt and cnt <= numMax:
        return True
    return False

def challenge(filename, validator):
    entries = readFile(filename)
    valid = 0
    for e in entries:
        if validator(e):
            valid += 1
    print("Counted " + str(valid) + " valid passwords.")

def isValidPassowrd2(s):
    cond, pwd = s.split(":")
    m = re.match("^(\d+)-(\d+) (\w)", cond)
    numOne = int(m.group(1))
    numTwo = int(m.group(2))
    letter = m.group(3)
    if numOne < 1 or numTwo < numOne or numTwo > len(pwd):
        return False
    elif pwd[numOne] == letter and pwd[numTwo] != letter:
        return True
    elif pwd[numOne] != letter and pwd[numTwo] == letter:
        return True
    return False

challenge("data/d2.txt", isValidPassword)
challenge("data/d2.txt", isValidPassowrd2)