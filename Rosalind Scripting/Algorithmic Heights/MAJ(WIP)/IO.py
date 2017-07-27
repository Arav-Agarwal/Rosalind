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
valueinputs = population[0]
values = valueinputs.split(" ")
commonlisttext = population[1:]
commonlist = commonlisttext.split(" ")
numberOfInts = values[1]
posmat = []
posdic = {}
while commonlist != []:
    currentlist = commonlist[0:(int(numberOfInts))]
    commonlist = commonlist[int(numberOfInt):]
    sumv = 0
    hist = {}
    for i in currentlist:
        if hist[i] 
foutput.write(True)
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write(str(int(num)+1))
fnumnew.close()
foutput.close()
finput.close()
