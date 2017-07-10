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
k = int(population[0]) # get input values from system. Here this is the number of generations
N = int(population[1]) # real code starts here. Here this is the required number of Tom-alikes
MGen = 2**k
prob = 0
for i in range(N):
    p1 = (choose(MGen,i)*(0.25**i)*(0.75**(MGen-i)))
    prob += p1
    print str(i) + " " + str(p1) + " " + str(prob)
foutput.write(str(1-prob))
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write(str(int(num)+1))
fnumnew.close()
foutput.close()
finput.close()
