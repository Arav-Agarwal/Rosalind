fnumcurrent = open('fileprogressnumber.txt', 'r') #filenumber reading
num = fnumcurrent.read()
fnumcurrent.close()
finput = open('input2.txt', 'r') #input reading
foutput = open('output' + num + '.txt', 'w') #input writing
text=finput.read()
splt=text.split() #splitting portions into a list
cyd = {}
for i in splt:    
    if i in cyd:
        cyd[i] += 1
    else:
        cyd[i] = 1
print(cyd)
for j in cyd:
    foutput.write(j + " " + str(cyd[j]) + "\n")
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write(str(int(num)+1))
fnumnew.close()
foutput.close()
finput.close()
