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
popul = text.split("\n")
strin = popul[0]
substr = popul[1]
wt = 0
currentlist = []
while (wt >= 0):
    wt = strin.find(substr,wt+1)
    if wt != -1:
        currentlist.append(str(wt+1))
final = ' '.join(currentlist)
print(final)
foutput.write(final)
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write(str(int(num)+1))
fnumnew.close()
foutput.close()
finput.close()
