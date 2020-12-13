DAY_NUM = 12


def input():
    f = open("input/day" + str(DAY_NUM) + ".txt")
    inp = [l.rstrip('\n') for l in f]
    f.close()
    return inp

def move(inp):
    x, y = 0, 0
    facing = 'E'

    for inst in inp:
        com, val = inst[0], int(inst[1:])
        if com == 'E':
            x += val
        elif com == 'N':
            y += val
        elif com == 'W':
            x -= val
        elif com == 'S':
            y -= val
        elif com == 'F':
            if facing == 'E':
                x += val
            elif facing == 'N':
                y += val
            elif facing == 'W':
                x -= val
            elif facing == 'S':
                y -= val
        elif com == 'L':
            if facing == 'E':
                if val == 90:
                    facing = 'N'
                elif val == 180:
                    facing = 'W'
                elif val == 270:
                    facing = 'S'
            elif facing == 'N':
                if val == 90:
                    facing = 'W'
                elif val == 180:
                    facing = 'S'
                elif val == 270:
                    facing = 'E'
            elif facing == 'W':
                if val == 90:
                    facing = 'S'
                elif val == 180:
                    facing = 'E'
                elif val == 270:
                    facing = 'N'
            elif facing == 'S':
                if val == 90:
                    facing = 'E'
                elif val == 180:
                    facing = 'N'
                elif val == 270:
                    facing = 'W'
        elif com == 'R':
            if facing == 'E':
                if val == 90:
                    facing = 'S'
                elif val == 180:
                    facing = 'W'
                elif val == 270:
                    facing = 'N'
            elif facing == 'N':
                if val == 90:
                    facing = 'E'
                elif val == 180:
                    facing = 'S'
                elif val == 270:
                    facing = 'W'
            elif facing == 'W':
                if val == 90:
                    facing = 'N'
                elif val == 180:
                    facing = 'E'
                elif val == 270:
                    facing = 'S'
            elif facing == 'S':
                if val == 90:
                    facing = 'W'
                elif val == 180:
                    facing = 'N'
                elif val == 270:
                    facing = 'E'
    return abs(x) + abs(y)
        

def waypoint(inp):
    x, y = 0, 0
    wpX, wpY = 10, 1

    for inst in inp:
        com, val = inst[0], int(inst[1:])
        xO = wpX - x
        yO = wpY - y
        if com == 'E':
            wpX += val
        elif com == 'N':
            wpY += val
        elif com == 'W':
            wpX -= val
        elif com == 'S':
            wpY -= val
        elif com == 'F':
            x += xO * val
            y += yO * val
            wpX += xO * val
            wpY += yO * val
        elif com == 'L':
            rot = 0
            if val == 90:
                rot = 1
            if val == 180:
                rot = 2
            if val == 270:
                rot = 3  
            for _ in range(rot):
                xO = wpX - x
                yO = wpY - y
                wpX = -yO + x
                wpY = xO + y
        elif com == 'R':
            rot = 0
            if val == 90:
                rot = 1
            if val == 180:
                rot = 2
            if val == 270:
                rot = 3  
            for _ in range(rot):
                xO = wpX - x
                yO = wpY - y
                wpX = yO + x
                wpY = -xO + y

    return abs(x) + abs(y)
    
def main():
    inp = input()

    answer1, answer2 = move(inp), waypoint(inp)
    print(f"Answer to question one: {answer1}\nAnswer to question two: {answer2}")


if __name__ == "__main__":
    main()
