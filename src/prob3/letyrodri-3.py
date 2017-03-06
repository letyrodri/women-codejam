# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def solve(c,v,l, tc):

    cant = int(l/2)
    tot = 0


    for i in range(0, cant+1):
        if i > 0:
            tot = tot + pow(v, l - i) * pow(c, i)*(round((l-i)/i))
        else:
            tot = tot + pow(v, l - i) * pow(c, i)

    return [tot]

t = int(input())  # read a line with a single integer
for tc in range(1, t + 1):
    c,v,l = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

    # if i == 94:
    res = solve(c,v,l, tc)

    print("Case #{}:".format(str(tc)), " ".join([str(x) for x in res]))
    # check out .format's specification for more formatting options
