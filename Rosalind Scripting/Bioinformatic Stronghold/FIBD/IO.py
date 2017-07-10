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
n = int(population[0]) # get input values from system. Here this is the number of months
m = int(population[1]) # real code starts here. Here this is the number of months for life
TBP = [1]
for i in range(m-1):
    TBP.append(0)
print(TBP)
for i in range(n-1):
    stor = TBP[0]
    nstor = sum(TBP[1:])
    hmm = True
    for j in range(len(TBP)):
        print(j)
        if j == 0:
            TBP[j] = nstor
            print("hi")
        elif hmm:
            nstor = TBP[j]
            TBP[j] = stor
            hmm = False
            print("hii")
        else:
            stor = TBP[j]
            TBP[j] = nstor
            hmm = True
            print("hiii")
    print(TBP)
foutput.write(str(sum(TBP)))
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write(str(int(num)+1))
fnumnew.close()
foutput.close()
finput.close()
