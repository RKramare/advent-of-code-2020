DAY_NUM = 14


def input():
    f = open("input/day" + str(DAY_NUM) + ".txt")
    inp = [l.rstrip('\n') for l in f]
    f.close()
    return inp


def doTheStuff(inp):
    addresses = {}
    mask, addr, val = "", "", ""
    for l in inp:
        if l[:4] == 'mask':
            mask = l[7:]
        else:
            addr, val = int(l[4:].split(']')[0]), str(bin(int(l[4:].split(']')[1].split(' ')[2])))[2:]
            tmp = "0"*(len(mask)-len(val)) + val
            addresses[addr] = moreStuff(tmp, mask)
    res = 0
    for addr in addresses.values():
        res += int(addr, 2)
    return res


def moreStuff(tmp, mask):
    res = ""
    for t, m in zip(tmp, mask):
        if m == 'X':
            res += t
        else:
            res += m
    return res


def main():
    inp = input()

    answer1, answer2 = doTheStuff(inp), 0
    print(f"Answer to question one: {answer1}\nAnswer to question two: {answer2}")


if __name__ == "__main__":
    main()
    