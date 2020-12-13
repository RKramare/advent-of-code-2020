DAY_NUM = 13


def input():
    f = open("input/day" + str(DAY_NUM) + ".txt")
    inp = [l.rstrip('\n') for l in f]
    f.close()
    time = int(inp[0])
    busses = inp[1].split(",")
    return time, busses


def timeTable(time, busses):
    allBusses = []
    for bus in busses:
        if not bus == 'x':
            allBusses.append(int(bus))
            
    nextBus = {}
    for bus in allBusses:
        nextTime = time+bus-time%bus
        #print(f"Bus {bus} leaves in {nextTime-time} minutes.")
        nextBus[bus] = nextTime-time
    answ = min(nextBus.items(), key=lambda x: x[1])
    return answ[0]*answ[1]

            
def otherTime(time, busses):
    return "no"


def main():
    time, busses = input()    

    answer1, answer2 = timeTable(time, busses), otherTime(timeTable, busses)
    print(f"Answer to question one: {answer1}\nAnswer to question two: {answer2}")


if __name__ == "__main__":
    main()
