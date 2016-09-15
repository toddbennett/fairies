def reduce(x):
    n = x[0]
    d = x[1]
    if n % d == 0:
        n //= d
        d //= d
    for i in range(2, min(n,d)+1):
        while n % i == 0 and d % i == 0:
            n //= i
            d //= i
    return (n,d)

def sortFracs(fracs):
    if len(fracs) <= 1:
        return fracs
    p = fracs[-1]
    np = 1
    small = []
    big = []
    for f in fracs[:-1]:
        c = compFracs(f,p)
        if c == 1:
            big.append(f)
        elif c == -1:
            small.append(f)
        else:
            np += 1
    return sortFracs(small) + [p] + sortFracs(big)

def compFracs(f,p):
    f0 = f[0] * p[1]
    p0 = p[0] * f[1]
    if f0 < p0:
        return -1
    elif f0 > p0:
        return 1
    else:
        return 0

def genFracs(m):
    fracs = []

    for d in range(1, m+1):
        for n in range(d+1):
            if (n,d) == reduce((n,d)):
                fracs.append((n,d))
    return fracs

def genFracsRecursive(m):
    if m == 0:
        return []
    if m == 1:
        return [(0,1),(1,1)]
    prev = genFracsRecursive(m-1)
    fracs = []
    for i in range(len(prev)-1):
        fracs.append(prev[i])
        f = freshmanAdd(prev[i], prev[i+1])
        #if f[1] <= m:
        fracs.append(f)
    fracs.append(prev[-1])
    return fracs

def printFracs(fracs):
    for f in fracs:
        print(str(f[0]) + '/' + str(f[1]), end=', ')
    print()

def freshmanAdd(f, g):
    return reduce((f[0]+g[0],f[1]+g[1]))

def testFracs(fracs):
    for i in range(len(fracs)-2):
        f = fracs[i]
        g = fracs[i+2]
        if compFracs(freshmanAdd(f,g),fracs[i+1]) != 0:
            print("FAILURE!", f, "++", g, "=", freshmanAdd(f,g), "=/=", fracs[i+1])
            return False
    print("Tyson's theorem holds for this data set")
    return True

def prime(p):
    for i in range(2,p):
        if p % i == 0:
            return False
    return True

def commonDenom(fracs):
    d = 1
    for f in fracs:
        if d%f[1] != 0:
            x = reduce((d,f[1]))
            d *= x[1]
    return d

def denomFracs(fracs):
    d = commonDenom(fracs)
    for i in range(len(fracs)):
        f0 = fracs[i][0]*d//fracs[i][1]
        f1 = d
        fracs[i] = (f0,f1)

def printDifs(fracs):
    for i in range(len(fracs)-1):
        print(fracs[i+1][0] - fracs[i][0], end=', ')
    print()
        
for i in range(11):
    fracs = sortFracs(genFracs(i))
    altfracs = genFracsRecursive(i)
    printFracs(fracs)
    testFracs(fracs)
    printFracs(altfracs)
    testFracs(altfracs)
    print()
    denomFracs(fracs)
    printFracs(fracs)
    print()
    printDifs(fracs)
    print()
    print("---")
    print()
