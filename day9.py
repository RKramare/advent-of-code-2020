DAY_NUM = 9


def input():
    f = open("input/day" + str(DAY_NUM) + ".txt")
    inp = [int(l.rstrip('\n')) for l in f]
    f.close()
    return inp


def canSum(n, preamble):
    for i in range(len(preamble)):
        for j in range(len(preamble)):
            if preamble[i] + preamble[j] == n:
                return True
    return False


def findFaulty(inp, preSize):
    preamble = [inp[i] for i in range(preSize)]
    numbers = inp[preSize:]

    for n in numbers:
        if canSum(n, preamble):
            preamble = preamble[1:]
            preamble.append(n)
            numbers = numbers[1:]
        else:
            return n
     

def contiguous(inp, preSize, n):
    numbers = inp[:]
    i = 0
    while i < len(numbers):
        conSet = []
        j = i
        while sum(conSet) < n:
            conSet.append(numbers[j])
            if sum(conSet) == n:
                return min(conSet) + max(conSet)
            j += 1
        i += 1


def main():
    inp = input()
    preSize = 25

    n = findFaulty(inp, preSize)
    m = contiguous(inp, preSize, n)

    answer1, answer2 = n, m
    print(f"Answer to question one: {answer1}\nAnswer to question two: {answer2}")


if __name__ == "__main__":
    main()
