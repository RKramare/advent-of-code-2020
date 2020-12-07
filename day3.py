DAY_NUM = 3


def input():
    f = open("input/day" + str(DAY_NUM) + ".txt")
    inp = [l.rstrip('\n') for l in f]
    f.close()
    return inp

def pritnMap(inp):
    for e in inp:
        print(e)


def findTreesInSlope(inp, startX, startY, sizeX, sizeY, jumpX, jumpY):

    print(f"Grid of x,y: {sizeX},{sizeY} with jump x,y: {jumpX},{jumpY}")

    trees = 0
    x = startX
    for y in range(startY+jumpY, sizeY, jumpY):
        x += jumpX
        if x >= sizeX:
            x = x - sizeX

        #if inp[y][x] == ".":
        #    inp[y] = inp[y][:x] + "O" + inp[y][x+1:]

        if inp[y][x] == "#":
            trees += 1
        #    inp[y] = inp[y][:x] + "X" + inp[y][x+1:]
    
    return trees

def treeProds(inp, startX, startY, sizeX, sizeY):
    prod = 1
    for i in range(1,8,2):
        trees = findTreesInSlope(inp, startX, startY, sizeX, sizeY, i, 1)
        print(trees)
        prod *= trees
    trees = findTreesInSlope(inp, startX, startY, sizeX, sizeY, 1, 2)
    print(trees)
    prod *= trees
    return prod

def main():
    inp = input()
    
    startX = 0
    startY = 0
    sizeX = len(inp[0])
    sizeY = len(inp)

    jumpX = 3
    jumpY = 1

    print()
    answer1 = findTreesInSlope(inp, startX, startY, sizeX, sizeY, jumpX, jumpY)
    answer2 = treeProds(inp, startX, startY, sizeX, sizeY)
    print(f"Answer to question one: {answer1}\nAnswer to question two: {answer2}")


if __name__ == "__main__":
    main()
