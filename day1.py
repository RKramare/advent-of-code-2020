DAY_NUM = 1


def input():
    f = open("input/day" + str(DAY_NUM) + ".txt")
    inp = [l.rstrip('\n') for l in f]
    f.close()
    return inp


def sumsTo2020(n1, n2, n3 = 0):
    return n1 + n2 + n3 == 2020


def twoSums(inp):
    for i in range(len(inp)):
        for j in range(len(inp)):
            n1, n2 = int(inp[i]), int(inp[j])
            if sumsTo2020(n1, n2):
                #print("First:", n1, "Second:", n2, "Sum:", n1*n2)
                return n1*n2


def threeSums(inp):
    for i in range(len(inp)):
        for j in range(len(inp)):
            for k in range(len(inp)):
                n1, n2, n3 = int(inp[i]), int(inp[j]), int(inp[k])
                if sumsTo2020(n1, n2, n3):
                    #print("First:", n1, "Second:", n2, "Third:", n3, "Sum:", n1*n2*n3)
                    return n1*n2*n3


def main():
    inp = input()
    answer1 = twoSums(inp)
    answer2 = threeSums(inp)
    print(f"Answer to question one: {answer1}\nAnswer to question two: {answer2}")


if __name__ == "__main__":
    main()
