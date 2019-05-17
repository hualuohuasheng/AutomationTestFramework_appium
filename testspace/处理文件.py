# -*- coding:utf-8 -*-

import re

filename = "e://超级军工帝国.txt"
filename = "e://1.txt"

f = open(filename,'r+',encoding='utf-8')
lines = f.readlines()
# print(lines)

f1 = open('e://2.txt','w+',encoding='utf-8')
for line in lines:
    # line.strip()
    res = re.findall('^第Hk\d+',line)
    if len(res) > 0:
        # print(lines.index(line))
        res_temp = res[0] + '章'
        line= re.sub('^第Hk\d+',res_temp,line)
        print(line)
    f1.write(line)
f1.close
    # s = re.split('^\d+\b',line)
    # print(s)
