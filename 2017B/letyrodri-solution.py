# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def solve(case, roles, probs):
    probs.sort()
    
    sroles = probs[0:roles]
    froles = probs[roles:len(probs)][::-1]
    
    total = 1
    for i in range(0,roles):
        total = total*(1-(froles[i]*sroles[i]))
    
    return total 


t = int(input())  # case qty
for case in range(1, t + 1):
    # Single Int: int(input())
    # Many Int: [int(s) for s in input().split(" ")]
    
    roles = int(input())  
    probs = [float(s) for s in input().split(" ")]
        
    solution = solve(case, roles, probs)

    print("Case #{}: ".format(str(case))+str(solution))    