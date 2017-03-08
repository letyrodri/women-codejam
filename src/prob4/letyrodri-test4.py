import sys


def isSolution(probIn, probOut, caseId):
    if not probOut == "IMPOSSIBLE":
        for p in probIn[1]:
            if p in probOut:
                print(p)
                return False
    return True

file = sys.argv[1]

fileIn = file+".in"
fileOut = file+".out"


with open(fileIn) as fIn:  
    with open(fileOut) as fOut:
        t = int(fIn.readline())
        for i in range(1, t+1):
            probIn = [int(fIn.readline()), [x for x in fIn.readline().split()]]

            probOut = fOut.readline()
            caseId = probOut.split(":")[0]
            probOut = probOut.split(":")[1].strip()

            print(caseId)
            print(isSolution(probIn,probOut,caseId))