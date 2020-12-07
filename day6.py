DAY_NUM = 6


def input():
    f = open("input/day" + str(DAY_NUM) + ".txt")
    inp = [l.rstrip('\n') for l in f]
    f.close()
    return inp

def getForms(inp):
    forms = []
    form = ""
    for l in inp:
        if l:
            form += l
        else:
            forms.append(form)
            form = ""
    forms.append(form)
    return forms

def getIndForms(inp):
    forms = []
    form = []
    for l in inp:
        if l:
            form.append(l)
        else:
            forms.append(form)
            form = []
    forms.append(form)
    #print(forms)
    return forms


def allYes(indForm):
    count = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
        
    for f in indForm:
        #print(f)
        for c in alphabet:
            allY = True
            for i in f:
                if not c in i:
                    allY = False
                    break
            if allY:
                #print(i)
                count += 1
        #print()
    return count


def findYes(forms):
    count = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for f in forms:
        for c in alphabet:
            if c in f:
                #print(c)
                count += 1
        #print()
    return count



def main():
    inp = input()

    forms = getForms(inp)
    indForms = getIndForms(inp)

    #print(forms)

    answer1, answer2 = findYes(forms), allYes(indForms)
    print(f"Answer to question one: {answer1}\nAnswer to question two: {answer2}")


if __name__ == "__main__":
    main()
