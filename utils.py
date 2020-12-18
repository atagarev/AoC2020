def readFile(filename):
    lines = []
    with open(filename, encoding="utf-8") as f:
        for l in f:
            lines.append(l.strip())
    return lines