# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def allTrue(d):
    for k in d.keys():
        if not d.get(k):
            return False

    return True


def getFalse(d):
    for k in d.keys():
        if not d.get(k):
            return k

    return None

def dfs(d):
    res = []

    nodes = d.keys()
    visited = dict()

    for n in nodes:
        visited[n] = False

    q = list()


    while(not allTrue(visited)):
        if len(q) == 0:
            q.append(getFalse(visited))

        n = q.pop()
        res.append(n)
        visited[n] = True
        ady = d[n]
        for a in ady:
            if not visited[a]:
                q.append(a)

    return res

def repite(p):
    countL = dict()

    for l in p:

        if l not in countL.keys():
            countL[l] = 0

        countL[l] = countL[l]+1

        if countL[l] > 1:
            return True

    return False

def solve(n, pwds, tc):
    rel = dict()

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    setLetters = set([s for s in letters])

    for l in letters:
        rel[l] = set()

    for p in pwds:
        pass
    if len(p) == 1:
        return "IMPOSSIBLE"
    else:
        i = 0
        while (i < len(p)-1):
            l = p[i]
            rel[l].add(p[i+1])
            i=i+1

    listAdy = dict()

    for r in rel.keys():
        rel[r].add(r)
        listAdy[r] = setLetters.difference(rel.get(r))


    return "".join(dfs(listAdy))



t = int(input())  # read a line with a single integer
for tc in range(1, t + 1):
    n =  int(input())
    p = [s for s in input().split(" ")]  # read a list of integers, 2 in this case

    # if i == 94:

    res = solve(n,p, tc)

    print("Case #{}:".format(str(tc)), res)
    # check out .format's specification for more formatting options
