DAY_NUM = 4


def input():
    f = open("input/day" + str(DAY_NUM) + ".txt")
    #f = open("input/passp.txt")
    inp = [l.rstrip('\n') for l in f]
    f.close()
    print(inp)
    return inp


def getPasses(inp):
    inp.append('')
    tmp = ""
    passes = []
    for l in inp:
        if not l:
            tmp = tmp.split(" ")
            #print(tmp)
            cPass = {}

            for elem in tmp:
                if elem:
                    t = elem.split(":")
                    #print(t)
                    cPass[t[0]] = t[1]
            passes.append(cPass)

            tmp = ""
        else:
            tmp += " " + l

    return passes

def is_int(val):
    try:
        int(val)
    except ValueError:
        return False
    return True

def is_hex(val):
    try:
        int(val, 16)
    except ValueError:
        return False
    return True

def isVaildPass(p):
    if not (int(p["byr"]) >= 1920 and int(p["byr"]) <= 2002): return False
    if not (int(p["iyr"]) >= 2010 and int(p["iyr"]) <= 2020): return False
    if not (int(p["eyr"]) >= 2020 and int(p["eyr"]) <= 2030): return False
    if p["hgt"][-2:] == "cm":
        if not (int(p["hgt"][:-2]) >= 150 and int(p["hgt"][:-2]) <= 193): return False
    elif p["hgt"][-2:] == "in":
        if not (int(p["hgt"][:-2]) >= 59 and int(p["hgt"][:-2]) <= 76): return False
    else:
        return False
    if not (p["hcl"][0] == "#" and len(p["hcl"]) == 7 and is_hex(p["hcl"][1:])): return False  
    if not (p["ecl"] == "amb" or p["ecl"] == "blu" or p["ecl"] == "brn" or p["ecl"] == "gry" or p["ecl"] == "grn" or p["ecl"] == "hzl" or p["ecl"] == "oth"): return False
    if not len(p["pid"]) == 9 or not is_int(p["pid"]): return False
    
    return True


def countValidPasses(inp):
    passes = getPasses(inp)
    count, strict = 0, 0
    for cPass in passes:
        if len(cPass) == 8 or (len(cPass) == 7 and not "cid" in cPass):
            count += 1
            if isVaildPass(cPass): strict += 1
        
    return count, strict

def main():
    inp = input()
    print(is_hex("#ab123a"[1:]))

    print("#ab123a"[1:])

    answer1, answer2 = countValidPasses(inp)
    print(f"Answer to question one: {answer1}\nAnswer to question two: {answer2}")


if __name__ == "__main__":
    main()
