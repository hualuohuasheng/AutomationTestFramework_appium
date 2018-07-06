import matplotlib.pyplot as plt
import numpy as np
#x = [1,2,3,4,5,4,3,3,2,55,3,2,2,1]
#plt.plot(x,color='red')
#plt.show()

filename = "f://logs/iroom/pslstreaming_log.txt"

delayms,iTargetDelay,curr_videobr,databr,networkbr= [],[],[],[],[]
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # print(line.rstrip())
    if 'CheckTransStatus' in line:
       s = line.split(" ")
       #print(len(s))
       delayms.append(int(s[13].split("/")[0]))
       iTargetDelay.append(int(s[29].split(",")[0]))
       curr_videobr.append(int(s[31].split(",")[0]))
       databr.append(int(s[33].split(",")[0]))
       networkbr.append(s[35].split(",")[0])
       #print(s)
       #print(s[13].split("/")[0])
       
       
#print(delayms,iTargetDelay,curr_videobr,databr,networkbr)
#print(iTargetDelay)

plt.plot(delayms,color='red')
plt.plot(iTargetDelay,color='green', linewidth=5.0, linestyle='-')
plt.plot(curr_videobr,color='yellow')
plt.plot(databr,color='black')
plt.show()