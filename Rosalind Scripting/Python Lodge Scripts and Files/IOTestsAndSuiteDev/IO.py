fnumcurrent = open('fileprogressnumber.txt', 'r')
num = fnumcurrent.read()
fnumcurrent.close()
finput = open('input.txt', 'r')
foutput = open('output' + num + '.txt', 'w')
linenum = 0
text=finput.read()
splt=text.splitlines()
for i in splt:
    linenum += 1    
    if linenum%2 == 0:
        foutput.write(str(i) + '\n')
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write(str(int(num)+1))
fnumnew.close()
foutput.close()
finput.close()
