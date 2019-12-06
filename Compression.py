test = [1, 2, 3, 1, 2, 1, 2, 3, 1, 2, 4, 5]
patterns = dict()
repeats = dict()

def findPatterns(a):
    i = len(a) // 2
    for n in range(2, i + 1)[::-1]:
        potential = []
        for x in range(len(a) - n + 1):
            if (x >= n or len(a) - (x + n) >= n):
                search = a[x:x + n]
                if search not in potential:
                    potential += [search]
                else:
                    if (search in patterns.values()):
                        key = list(patterns.keys())[list(patterns.values()).index(search)]
                    else:
                        key = 'p' + str(len(patterns))
                        patterns[key] = search
                    return replace(a, search, [key])
    return a
    
def replace(arr, search, replace):
    for x in range(len(arr) - len(search) + 1):
        if (arr[x:x + len(search)] == search):
            arr = arr[0:x] + replace + arr[x + len(search):]
    return arr

def findRepeats(a):
    lastel = tuple()
    replaces = 0
    for i, x in enumerate(a):
        if (lastel and lastel[0] == x):
            lastel = (x, lastel[1], lastel[2] + 1)
        else:
            if (lastel and lastel[2] > 2):
                value = (lastel[0], lastel[2])
                if (value in repeats.values()):
                    key = list(repeats.keys())[list(repeats.values()).index(value)]
                else:
                    key = 's' + str(len(repeats))
                    repeats[key] = value
                a = a[0:lastel[1]] + [key] + a[lastel[1] + lastel[2]:]
                replaces += lastel[2] - 1
            lastel = (x, i - replaces, 1)
    if (lastel and lastel[2] > 2):
        value = (lastel[0], lastel[2])
        if (value in repeats.values()):
            key = list(repeats.keys())[list(repeats.values()).index(value)]
        else:
            key = 's' + str(len(repeats))
            repeats[key] = value
        a = a[0:lastel[1]] + [key] + a[lastel[1] + lastel[2]:]
    return a

def compress(a):
    print("Input:\n", a)
    a = [str(x) for x in a]
    newPattern = False
    origlength = len(a)
    origa = []

    while (a != origa):
        origa = [x for x in a]
        a = findRepeats(a)
        a = findPatterns(a)
        if (a != origa):
            newPattern = True
    
    while (newPattern):
        newPattern = False
        for key in list(patterns):
            origp = []
            while (patterns[key] != origp):
                origp = [x for x in patterns[key]]
                patterns[key] = findPatterns(patterns[key])
                if (patterns[key] != origp):
                    newPattern = True
    print("Output:\n", a)
    print("Compressed by " + str(100 * (1 - (len(a) + len(patterns) + len(repeats)) / origlength)) + '%')
    #print(patterns)
    #print(repeats)
    return a

def extract(a):
    while('p' in ' '.join(a) or 's' in ' '.join(a)):
        for key in patterns:
            a = replace(a, [key], patterns[key])
        for key in repeats:
            a = replace(a, [key], [repeats[key][0]] * repeats[key][1])
    return [int(x) for x in a]
            
