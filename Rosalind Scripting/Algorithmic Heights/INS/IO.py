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
n = population[0]
commonlisttext = " ".join(population[1:])
commonlist = commonlisttext.split(" ")
swaps = 0
for i in range(2,int(n)):
    k = i
    while k <= i and commonlist[k-1] < commonlist[k-2]:
        print(commonlist[k-1]  + " " + commonlist[k-2])
        temp = commonlist[k-1]
        commonlist[k-1] = commonlist[k-2]
        commonlist[k-2] = temp
        swaps += 1
        k -= 1
print(swaps)
print(commonlist)
foutput.write(True)
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write(str(int(num)+1))
fnumnew.close()
foutput.close()
finput.close()
