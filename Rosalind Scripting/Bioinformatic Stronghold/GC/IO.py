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
for j in population:
    temp = j.split("\n")
    tem = temp[1:]
    fastD[temp[0]] = ''.join(tem)
for k in fastD:
    G = fastD[k]
    suu = 0
    for l in G:
        if l == 'G' or l == 'C':
            suu += 1
    GC = suu/len(G)
    fastD[k] = GC
maa = 0
mal = ""
print(fastD)
for k in fastD:
    if fastD[k] > maa:
        maa = fastD[k]
        mal = k
print(maa)
print(mal)
foutput.write(mal + "\n" + str(maa*100))
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write(str(int(num)+1))
fnumnew.close()
foutput.close()
finput.close()
