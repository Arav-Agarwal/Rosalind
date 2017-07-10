import os
fnumcurrent = open('fileprogressnumber.txt', 'r') #filenumber reading
print fnumcurrent
num = fnumcurrent.read()
fnumcurrent.close()
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write('1')
fnumnew.close()
for i in range(1,int(num)):
    os.remove("input" + str(i) + ".txt")
    os.remove("output" + str(i) + ".txt")
