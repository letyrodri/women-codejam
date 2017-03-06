# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def solve(d,k,n, tc):

    dancers = [j for j in range(1, d+1)]

    for i in range(1, n+1):

        if i % 2 == 0:
            # even
            dancers = swap_counterclockwise(dancers,d)
        else:
            # odd
            dancers = swap_clockwise(dancers, d)


    return get_neighbours(dancers,k)

def swap_clockwise(l,d):
    i = 0
    while(i < len(l)):
        l[i], l[i+1] = l[i+1], l[i]
        i=i+2
    return l


def swap_counterclockwise(l,d):
    l[0], l[d-1] = l[d-1], l[0]
    i = d-2
    while(i >= 1):
        l[i], l[i-1] = l[i-1], l[i]
        i=i-2
    return l

def get_neighbours(l,k):
    p = l.index(k)

    if p == len(l)-1:
        return (l[0],l[p-1])

    if p == 0:
        return (l[1],l[len(l)-1])

    return(l[p+1],l[p-1] )

t = int(input())  # read a line with a single integer
for tc in range(1, t + 1):
    d,k,n = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

    # if i == 94:
    res = solve(d,k,n, tc)

    print("Case #{}:".format(str(tc)), " ".join([str(x) for x in res]))
    # check out .format's specification for more formatting options
