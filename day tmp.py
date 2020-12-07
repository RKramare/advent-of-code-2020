DAY_NUM = 1


def input():
    f = open("input/day" + str(DAY_NUM) + ".txt")
    inp = [l.rstrip('\n') for l in f]
    f.close()
    return inp


def main():
    inp = input()
    print(inp)

    answer1, answer2 = 0, 0
    print(f"Answer to question one: {answer1}\nAnswer to question two: {answer2}")


if __name__ == "__main__":
    main()
