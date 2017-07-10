fnumcurrent = open('fileprogressnumber.txt', 'r') #filenumber reading
num = fnumcurrent.read()
fnumcurrent.close()
finput = open('input' + num + '.txt', 'r') #input reading
foutput = open('output' + num + '.txt', 'w') #input writing
text=finput.read()
reverse = text[::-1]
complement = ""
for i in reverse:
    if i == 'A':
        complement += "T"
    if i == 'C':
        complement += "G"
    if i == 'G':
        complement += "C"
    if i == 'T':
        complement += "A"
foutput.write(complement)
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write(str(int(num)+1))
fnumnew.close()
foutput.close()
finput.close()
