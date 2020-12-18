import re
from enum import Enum

from utils import readFile

class PassportField(Enum):
    BirthYear = "byr"
    IssueYear = "iyr"
    ExpirationYear = "eyr"
    Height = "hgt"
    HairColor = "hcl"
    EyeColor = "ecl"
    PassportId = "pid"
    CountryId = "cid"

    def getFieldByName(v):
        for field in PassportField:
            if field.value == v:
                return field
        return None

    def isRequired(self):
        return self != PassportField.CountryId

    def __str__(self):
        return self.value

class Passport():

    def __init__(self):
        self.fields = dict()

    def isValid(self):
        for fid in PassportField:
            if fid.isRequired():
                if not self.fields.__contains__(fid):
                    return False
                if fid == PassportField.BirthYear:
                    byr = int(self.fields[fid])
                    if byr < 1920 or byr > 2002:
                        return False
                elif fid == PassportField.IssueYear:
                    iyr = int(self.fields[fid])
                    if iyr < 2010 or iyr > 2020:
                        return False
                elif fid == PassportField.ExpirationYear:
                    eyr = int(self.fields[fid])
                    if eyr < 2020 or eyr > 2030:
                        return False
                elif fid == PassportField.Height:
                    hgh = self.fields[fid].strip()
                    m = re.match("^(\d+)(cm|in)", hgh)
                    if m is None:
                        return False
                    elif m.group(2) == "cm":
                        cms = int(m.group(1))
                        if 150 > cms or cms > 193:
                            return False
                    elif m.group(2) == "in":
                        inches = int(m.group(1))
                        if 59 > inches or inches > 75:
                            return False
                    else:
                        return False
                elif fid == PassportField.HairColor:
                    hcl = self.fields[fid].strip()
                    m = re.match("^#[0-9abcdef]{6}$", hcl)
                    if m is None:
                        return False
                elif fid == PassportField.EyeColor:
                    ecl = self.fields[fid].strip()
                    clrs = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                    if not clrs.__contains__(ecl):
                        return False
                elif fid == PassportField.PassportId:
                    pid = self.fields[fid].strip()
                    m = re.match("^[0-9]{9}$", pid)
                    if m is None:
                        return False

        return True

    def addField(self, text):
        f, v = text.split(":")
        fid = PassportField.getFieldByName(f)
        if fid is None:
            raise ValueError("Unknown passport field encountered: " + str(f))
        # elif not self.fields.__contains__(fid):
        #     raise ValueError("Trying to input value for " + str(fid) + " but that field already has a value.")
        self.fields[fid] = v

    def getValue(self, fid):
        if not self.fields.__contains__(fid):
            raise ValueError("Attempting to retrieve value for missing field " + str(fid))
        return self.fields[fid]

    def __str__(self):
        resp = ""
        for fid in self.fields:
            resp += str(fid) + " : " + self.fields[fid] + " ## "
        return resp

def challenge(lines):
    validCnt = 0
    passport = Passport()
    for line in lines:
        if line.strip() == "":
            if passport.isValid():
                validCnt += 1
            passport = Passport()
        else:
            for item in line.strip().split(" "):
                passport.addField(item)
    if passport.isValid():
        validCnt += 1
    return validCnt


lines = readFile("data/d4.txt")
# for line in lines:
    # if line.strip() == "":
        # print("Empty")
validCnt = challenge(lines)
print("Total valid passports: " + str(validCnt))