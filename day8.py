from enum import Enum

from utils import readFile

class Operation(Enum):
    ACC = "acc"
    NOP = "nop"
    JUMP = "jmp"

    def getOperationByName(v):
        for op in Operation:
            if op.value == v:
                return op
        return None

class Instruction():

    def __init__(self, line):
        op, num = line.strip().split(" ")
        self.operation = Operation.getOperationByName(op)
        self.operand = int(num)

    def getOperation(self):
        return self.operation

    def getOperand(self):
        return self.operand

class Program:

    LOOP_ENCOUNTERED = False

    def __init__(self, code):
        self.code = code
        self.accumulator = 0
        self.executedLines = set()

    def executeOperationv1(self, line):
        if not isinstance(line, int) or line <  0 or line >= len(self.code):
            raise ValueError("Invalid line execution requested {}".format(line))
        if self.executedLines.__contains__(line):
            return self.accumulator
        self.executedLines.add(line)
        instruction = self.code[line]
        if instruction.getOperation() == Operation.NOP:
            return self.executeOperationv1(line+1)
        elif instruction.getOperation() == Operation.JUMP:
            return self.executeOperationv1(line+instruction.getOperand())
        elif instruction.getOperation() == Operation.ACC:
            self.accumulator += instruction.getOperand()
            return self.executeOperationv1(line+1)
        else:
            raise ValueError("Unexpected operation type {} encountered.".format(instruction.getOperation()))

    def executeOperationv2(self, line, usedChange, acc):
        if not isinstance(line, int) or line <  0 or line > len(self.code):
            raise ValueError("Invalid line execution requested {}".format(line))
        elif line == len(self.code):
            print("Successful termination!")
            return acc
        if self.executedLines.__contains__(line):
            print("Encountered loop on line {}".format(line))
            return self.LOOP_ENCOUNTERED
        self.executedLines.add(line)
        instruction = self.code[line]
        if instruction.getOperation() == Operation.NOP:
            resp = self.executeOperationv2(line+1, usedChange, acc)
            if resp == self.LOOP_ENCOUNTERED and not usedChange:
                print("Trying to change line {} from NOP to JMP".format(line))
                resp = self.executeOperationv2(line+instruction.getOperand(), True, acc)
        elif instruction.getOperation() == Operation.JUMP:
            resp = self.executeOperationv2(line+instruction.getOperand(), usedChange, acc)
            if resp == self.LOOP_ENCOUNTERED and not usedChange:
                print("Trying to change line {} from JMP to NOP.".format(line))
                resp = self.executeOperationv2(line+1, True, acc)
        elif instruction.getOperation() == Operation.ACC:
            acc += instruction.getOperand()
            resp = self.executeOperationv2(line+1, usedChange, acc)
        else:
            raise ValueError("Unexpected operation type {} encountered.".format(instruction.getOperation()))
        return resp

if __name__ == "__main__":
    lines = readFile("data/d8.txt")
    instructions = []
    for line in lines:
        instructions.append(Instruction(line))
    prog = Program(instructions)
    acc = prog.executeOperationv1(0)
    print("Running version 1 gave a total accumulator value of {}.".format(acc))
    prog2 = Program(instructions)
    acc2 = prog2.executeOperationv2(0, False, 0)
    print("Running version 2 gave a total accumulator value of {}.".format(acc2))