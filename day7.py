DAY_NUM = 7


def input():
    f = open("input/day" + str(DAY_NUM) + ".txt")
    inp = [l.rstrip('\n') for l in f]
    f.close()
    return inp


def getBags(inp):
    bagNumDict = {}
    bagDict = {}
    for l in inp:
        l = l.split(" ")
        bag = l[0] + " " + l[1]
        l = l[4:]
        holds = []
        dictHolds = []
        while l:
            if l[0] == 'no':
                holds.append((0, "no other"))
                dictHolds.append("no other")
                l = l[3:]
            else:
                bagNum = int(l[0])
                bagColor = l[1] + " " + l[2]
                holds.append((bagNum, bagColor))
                dictHolds.append(bagColor)
                l = l[4:]
        bagNumDict[bag] = holds
        bagDict[bag] = dictHolds
    return bagNumDict, bagDict


def thereIsAGoldenBagInHereSomewhere(bagDict, contains):
    if not contains or contains[0] == 'no other':
        return False
    elif 'shiny gold' in contains:
        return True
    return thereIsAGoldenBagInHereSomewhere(bagDict, contains[1:]) or thereIsAGoldenBagInHereSomewhere(bagDict, bagDict[contains[0]])


def goldBags(bagDict):
    foundBags = set()
    for bag, contains in bagDict.items():
        if thereIsAGoldenBagInHereSomewhere(bagDict, contains):
            foundBags.add(bag)
    return len(foundBags)


# [(num, col), ...
def bagCol(bag):
    return bag[0][1]
# [(num, col), ...
def bagNum(bag):
    return bag[0][0]

def countBagsInGold(bagNumDict, contains):
    if not contains or bagCol(contains) == 'no other':
        return 0
    count = 0
    for _ in range(bagNum(contains)):
        count += countBagsInGold(bagNumDict, bagNumDict[bagCol(contains)])
    return bagNum(contains) + countBagsInGold(bagNumDict, contains[1:]) + count
    

def inGoldBag(bagNumDict):
    contains = bagNumDict['shiny gold']
    count = countBagsInGold(bagNumDict, contains)
    return count


def main():
    inp = input()
    bagNumDict, bagDict = getBags(inp)
    answer1, answer2 = goldBags(bagDict), inGoldBag(bagNumDict)
    print(f"Answer to question one: {answer1}\nAnswer to question two: {answer2}")


if __name__ == "__main__":
    main()
