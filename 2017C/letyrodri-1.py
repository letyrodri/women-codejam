# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def solve(d,n, tc):
    sale_price = []
    regular_price = []
    unknown = []
    res = []
    l=0
    line = ""
    res=""

    while (n >= 0):
        if l % 2 == 0:
            for i in range(0,min(n+1,7)):
                if l % 2 == 0:
                    if i == 0:
                        line = "I"
                    else:
                        if i % 2 == 1:
                            line = line + "/O"
                        else:
                            line = line + "/I"

            n = n - 6
            while(len(line) < 14):
                line = line+"I"
        else:
            line = "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII"

        l=l+1
        res = res+line+"\n"

    return res


t = int(input())  # read a line with a single integer
for tc in range(1, t + 1):
    d,n = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

    # if i == 94:
    res = solve(d,n, tc)

    print("Case #{}:".format(str(tc)))
    print(res[:-1])
    # check out .format's specification for more formatting options
