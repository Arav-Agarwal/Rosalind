#from __future__ import division
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
population = text.split("\n")
numsorted = population[0]
numtosearch = population[1]
commonlisttext = population[2] + " " + population[3]
commonlist = commonlisttext.split(" ")
sortedlist = commonlist[0:int(numsorted)]
sortedlistslv = commonlist[0:int(numsorted)]
tosearch = commonlist[int(numsorted):]
posmat = []
posdic = {}
ind = 1
for i in sortedlist:
    posdic[i] = ind
    ind += 1
for i in tosearch:
    sortedlistslv = sortedlist
    index = (len(sortedlistslv)/2)
    middleval = sortedlistslv[index]
    while middleval != i:
        print(sortedlistslv)
        if len(sortedlistslv) == 1:
            posmat.append("LOL")
            break
        if middleval < i:
            index = (len(sortedlistslv)/2)
            middleval = sortedlistslv[index]
            sortedlistslv = sortedlistslv[index:]
        elif middleval > i:
            index = (len(sortedlistslv)/2)
            middleval = sortedlistslv[index]
            sortedlistslv = sortedlistslv[:index]
    if middleval == i:
        posmat.append(middleval)
final = []
for i in posmat:
    if str(i) == "LOL":
        final.append("-1")
    else:
        final.append(str(posdic[i]))
finalt = " ".join(final)                
print finalt
foutput.write(True)
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write(str(int(num)+1))
fnumnew.close()
foutput.close()
finput.close()
