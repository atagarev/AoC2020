from utils import readFile

def buildAdapterChain(adapters, input, target, steps):
    if input == target:
        return steps
    if adapters.__contains__(input+1):
        step = 1
    elif adapters.__contains__(input+2):
        step = 2
    elif adapters.__contains__(input+3) or input+3 == target:
        step = 3
    else:
        raise ValueError("No valid adaptor available from next step from {} to {}.".format(input, target))
    steps[step] += 1
    return buildAdapterChain(adapters, input+step, target, steps)

def countAdapterChains(adapters, input, target):
    if input+3 == target:
        return 1
    s = 0
    options = 0
    maxOption = 0
    if adapters.__contains__(input+1):
        options += 1
        maxOption = 1
    if adapters.__contains__(input+2):
        options += 1
        maxOption = 2
    if adapters.__contains__(input+3):
        options += 1
        maxOption = 3
    return options * countAdapterChains(adapters, input+maxOption, target)

if __name__ == "__main__":
    lines = readFile("data/d10.txt")
    adapters = set()
    for line in lines:
        adapters.add(int(line.strip()))
    input = 0
    target = max(adapters) + 3
    steps = dict()
    steps[1] = 0
    steps[2] = 0
    steps[3] = 0
    steps = buildAdapterChain(adapters, input, target, steps)
    for step in steps:
        print("We have {} instances of a step of {} jolts.".format(steps[step], step))
    print("Answer to part 1 is {}.".format(steps[1]*steps[3]))
    cnt = countAdapterChains(adapters, input, target)
    print("Answer to part 2 is {}.".format(cnt))