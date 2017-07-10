fnumcurrent = open('fileprogressnumber.txt', 'r') #filenumber reading
num = fnumcurrent.read()
fnumcurrent.close()
finput = open('input1.txt', 'r') #input reading
foutput = open('output' + num + '.txt', 'w') #input writing
text=finput.read()
cyd = {}
for i in text:    
    if i in cyd:
        cyd[i] += 1
    else:
        cyd[i] = 1
print(cyd)
foutput.write(str(cyd['A']) + " " + str(cyd['C']) + " " + str(cyd['G']) + " " + str(cyd['T']))
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write(str(int(num)+1))
fnumnew.close()
foutput.close()
finput.close()
