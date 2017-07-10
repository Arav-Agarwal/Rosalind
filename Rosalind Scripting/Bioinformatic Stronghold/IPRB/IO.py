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
population = text.split()
dominant = int(population[0]) # get population values from system
hetero = int(population[1])
recessive = int(population[2])
dd = (choose( dominant, 2)*1) # calculate expected number of those with dominant phenotype
hh = (choose( hetero, 2)*0.75)
rr = (choose( recessive, 2)*0)
dr = (dominant*recessive*1)
dh = (dominant*hetero*1)
rh = (recessive*hetero*0.5)
total = (dd + hh + rr + dr + dh + rh)/ choose((dominant+hetero+recessive),2) # divide by total to get probablity
foutput.write(str(total))
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write(str(int(num)+1))
fnumnew.close()
foutput.close()
finput.close()
