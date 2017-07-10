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
popl = ''.join(popul)
protmassdir = {'A': '71.03711', 'C': '103.00919', 'E': '129.04259', 'D': '115.02694', 'G': '57.02146', 'F': '147.06841', 'I': '113.08406', 'H': '137.05891', 'K': '128.09496', 'M': '131.04049', 'L': '113.08406', 'N': '114.04293', 'Q': '128.05858', 'P': '97.05276', 'S': '87.03203', 'R': '156.10111', 'T': '101.04768', 'W': '186.07931', 'V': '99.06841', 'Y': '163.06333'}
mass = 0
for i in popl:
    if i != ' ':
        mass += float(protmassdir[i])
print mass
foutput.write(str(mass))
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write(str(int(num)+1))
fnumnew.close()
foutput.close()
finput.close()
