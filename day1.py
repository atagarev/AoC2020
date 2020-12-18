def readFile(filename):
    entries = []
    with open(filename, encoding="utf-8") as f:
        for l in f:
            entries.append(int(l.strip()))
    return entries

def challenge1(filename, target):
    entries = readFile(filename)

    for i, x in enumerate(entries):
        for j in range(i+1, len(entries)):
            y = entries[j]
            if (x+y) == target:
                print("Challenge1: X: " + str(x) + " Y: " + str(y) + " X*Y: " + str(x*y))

def challenge2(filename, target):
    entries = readFile(filename)

    for i, x in enumerate(entries):
        for j, y in enumerate(entries, i+1):
            for k, z in enumerate(entries, j+1):
                if (x+y+z) == target:
                    print("Challenge2: X: "+ str(x) + " Y: " + str(y) + " Z: " + str(z) + " X*Y*Z: " + str(x*y*z))

challenge1("data/d1c1.txt", 2020)
challenge2("data/d1c1.txt", 2020)