import sys


def isSolution(probIn, probOut, caseId):
	res = list(probOut)
	for n in probOut:
		res.append(int(n*100/75))

	res.sort()
	isOk = res == probIn[1]
	
	if not isOk:
		print("caseId:", caseId)
		print("res: ",res)
		print("probIn: ",probIn[1])
		print("probOut: ",probOut)

	return isOk 

file = sys.argv[1]

fileIn = file+".in"
fileOut = file+".out"


with open(fileIn) as fIn:  
	with open(fileOut) as fOut:  
		t = int(fIn.readline())
		for i in range(1, t+1):
			probIn = [int(fIn.readline()), [int(x) for x in fIn.readline().split()]]

			probOut = fOut.readline()
			caseId = probOut.split(":")[0]
			probOut = [int(x) for x in probOut.split(":")[1].split()]
			
			print(isSolution(probIn,probOut,caseId))