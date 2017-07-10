import os
fnumcurrent = open('fileprogressnumber.txt', 'r') #filenumber reading
print fnumcurrent
num = fnumcurrent.read()
fnumcurrent.close()
fnumnew = open('fileprogressnumber.txt', 'w')
fnumnew.write(str(int(num)-1))
fnumnew.close()
os.remove("output" + str(int(num)-1) + ".txt")
