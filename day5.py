DAY_NUM = 5


def input():
    f = open("input/day" + str(DAY_NUM) + ".txt")
    inp = [l.rstrip('\n') for l in f]
    f.close()
    return inp


def boardingPasses(inp, rows, cols, mult):
    passes = []
    for bPass in inp:
        row = [y for y in range(rows)]
        col = [x for x in range(cols)]
        for c in bPass:
            if c == 'F':
                row = row[:len(row)//2]
            elif c == 'B':
                row = row[len(row)//2:]
            elif c == 'R':
                col = col[len(col)//2:]
            elif c == 'L':
                col = col[:len(col)//2]
            
        res = row[0] * mult + col[0]
        passes.append(res)
    return passes


def missingPass(passes):
    passes.sort()
    for pID in passes:
        if not pID + 1 in passes:
            return pID + 1


def main():
    inp = input()
    passes = boardingPasses(inp, 128, 8, 8)

    answer1, answer2 = max(passes), missingPass(passes)
    print(f"Answer to question one: {answer1}\nAnswer to question two: {answer2}")


if __name__ == "__main__":
    main()
