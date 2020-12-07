DAY_NUM = 2


def input():
    f = open("input/day" + str(DAY_NUM) + ".txt")
    inp = [l.rstrip('\n') for l in f]
    f.close()
    return inp


def checkPasswords(inp):
    res1, res2 = 0, 0
    for line in inp:
        x = line.split(" ")
        fir = int(x[0].split("-")[0])
        sec = int(x[0].split("-")[1])
        letter = x[1][0]
        word = x[2]
        
        if bool(word[fir-1] == letter) != bool(word[sec-1] == letter):
            res1 += 1

        if word.count(letter) >= fir and word.count(letter) <= sec:
            res2 += 1
            

    return res1, res2


def main():
    inp = input()
    
    answer1, answer2 = checkPasswords(inp)
    print(f"Answer to question one: {answer1}\nAnswer to question two: {answer2}")


if __name__ == "__main__":
    main()
