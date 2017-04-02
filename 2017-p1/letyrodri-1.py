# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def solve(s,f,locations):
    duplicates = []
    rowqty =[ 0 for k in range(0,s+1) ]

    for l1 in locations:
        rest = list(locations)
        rest.remove(l1)
        for l2 in rest:
            if l1 == l2 and l1 not in duplicates:
                duplicates.append(l1)

            if l1[0] == l2[1] and l1[1] == l2[0] and l1 not in duplicates and l2 not in duplicates:
                duplicates.append(l1)
                duplicates.append(l2)

    for l in duplicates:
        if l in locations:
            locations.remove(l)

    for l in locations:
        if (l[0] == l[1]):
            rowqty[l[0]-1] = rowqty[l[0]-1] + 1
        else:
            rowqty[l[1]-1] = rowqty[l[1]-1] + 1
            rowqty[l[0] - 1] = rowqty[l[0] - 1] + 1


    mqty = max(rowqty)

    return mqty




t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    f,s = [int(s) for s in input().split(" ")]
    locations = []
    for j in range(1,f+1):
        location = [int(a) for a in input().split(" ")]  # read a list of integers, 2 in this case
        locations.append(location)
        # if i == 94:
    res = solve(s,f,locations)

    print("Case #{}:".format(str(i)), str(res))
    # check out .format's specification for more formatting options
