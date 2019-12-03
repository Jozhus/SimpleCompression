test = [1, 2, 3, 1, 2, 1, 2, 3, 1, 2, 4, 5]
patterns = dict()

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
                    key = 'p' + str(len(patterns))
                    patterns[key] = search
                    return ' '.join(a).replace(' '.join(search), key).split(' ')
    return a
    

def compress(a):
    print("Input:\n", a)
    a = [str(x) for x in a]
    newPattern = False
    origa = []

    while (a != origa):
        origa = [x for x in a]
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
    print("Output:")
    print(a)
    print(patterns)
    return a

def extract(a):
    a = ' '.join(a)
    while('p' in a):
        for key in patterns:
            a = a.replace(key, ' '.join(patterns[key]))
    return [int(x) for x in a.split(' ')]
            
