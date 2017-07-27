from __future__ import division
import math #import section
def choose( a, b): #definition section
    aFact = math.factorial(a)
    bFact = math.factorial(b)
    ambFact = math.factorial(a-b)
    toReturn = aFact / (bFact*ambFact)
    return toReturn;
fnumcurrent = open('fileprogressnumber.txt', 'r') #filenumber reading
num = fnumcurrent.read()
fnumcurrent.close()
finput = open('input' + num + '.txt', 'r') #input reading
foutput = open('output' + num + '.txt', 'w') #input writing
text=finput.read()
popul = text.split(">")
population = popul[1:]
fastD = {}
maxtem = 0
for j in population:
    temp = j.split("\n")
    tem = temp[1:]
    temr = ''.join(tem)
    if len(temr) > maxtem:
        maxtem = len(temr)
    fastD[temp[0]] = temr
AProf = [0] * maxtem
CProf = [0] * maxtem
GProf = [0] * maxtem
TProf = [0] * maxtem
for k in fastD:
    index = 0
    for l in fastD[k]:
        if l == "A": AProf[index] += 1
        elif l == "C": CProf[index] += 1
        elif l == "G": GProf[index] += 1
        elif l == "T": TProf[index] += 1
        index += 1
maxlist = [None] * maxtem
for m in range(0,maxtem):
    if AProf[m] >= CProf[m] and AProf[m] >= GProf[m] and AProf[m] >= TProf[m]:
        maxlist[m] = "A"
    elif CProf[m] >= AProf[m] and CProf[m] >= GProf[m] and CProf[m] >= TProf[m]:
        maxlist[m] = "C"
    elif GProf[m] >= AProf[m] and GProf[m] >= CProf[m] and GProf[m] >= TProf[m]:
        maxlist[m] = "G"
    elif TProf[m] >= AProf[m] and TProf[m] >= GProf[m] and TProf[m] >= CProf[m]:
        maxlist[m] = "T"
consensus = ''.join(maxlist)
AProfJ = "A: "  + ' '.join([str(i) for i in AProf])
CProfJ = "C: "  + ' '.join([str(i) for i in CProf])
GProfJ = "G: "  + ' '.join([str(i) for i in GProf])
TProfJ = "T: "  + ' '.join([str(i) for i in TProf])
print(consensus)
print(AProfJ)
print(CProfJ)
print(GProfJ)
print(TProfJ)
foutput.write(consensus + "\n" + AProfJ + "\n"  + CProfJ + "\n"  + GProfJ + "\n"  + TProfJ)
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write(str(int(num)+1))
fnumnew.close()
foutput.close()
finput.close()
