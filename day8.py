DAY_NUM = 8


def input():
    f = open("input/day" + str(DAY_NUM) + ".txt")
    inp = [l.rstrip('\n') for l in f]
    f.close()
    return inp


def getInstructions(inp):
    instructions = []
    for l in inp:
        l = l.split(" ")
        op = l[0]
        arg = int(l[1][1:])
        if l[1][0] == '-':
            arg *= -1
        instructions.append((op, arg))
    return instructions


def changeInstruction(instructions, i, opChange):
    arg = instructions[i][1]
    newInstr = instructions[:]
    newInstr[i] = (opChange, arg)
    return newInstr


def fixGame(instructions):
    for i in range(len(instructions)):
        op = instructions[i][0]
        if op == 'nop' or op == 'jmp':
            if op == 'nop':
                newOp = 'jmp'
            else:
                newOp = 'nop'
            newInstr = changeInstruction(instructions, i, newOp)
            accumulator, end = runGame(newInstr)
            if end == len(instructions):
                return accumulator


def runGame(instructions):
    accumulator = 0
    runLines = []
    i = 0
    while i < len(instructions):
        if i in runLines:
            break
        runLines.append(i)
        op = instructions[i][0]
        arg = instructions[i][1]
        if op == 'nop':
            i += 1
        elif op == 'acc':
            accumulator += arg
            i += 1
        elif op == 'jmp':
            i += arg
    return accumulator, i


def main():
    inp = input()
    instructions = getInstructions(inp)
    accumulator, _ = runGame(instructions)

    answer1, answer2 = accumulator, fixGame(instructions)
    print(f"Answer to question one: {answer1}\nAnswer to question two: {answer2}")


if __name__ == "__main__":
    main()
