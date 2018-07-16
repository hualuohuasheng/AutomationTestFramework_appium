# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import math as math
import re

def var(list, avg):
    var1 = 0
    for i in list:
        var1 += float((i - avg) ** 2 * 1.0)
    var2 = (math.sqrt(var1 / (len(list) - 1) * 1.0))
    return var2


def average(list):
    avg = sum(list) / float(len(list) * 1.0)
    return avg

def get_info(filename="f://logs/pslstreaming_log.txt"):
    delayms, curr_videobr, databr, netbr = [], [], [], []

    f = open(filename)
    lines = f.readlines()
    for line in lines:
        line_index = line.find('CheckTransStatus -- delay')
        if line_index > 0:
            # print(line)
            st = re.split(r'\W+',line)
            delayms.append(int(st[st.index('delay')+1]))
            databr.append(int(st[st.index('databr')+1]))
            netbr.append(int(st[st.index('netbr')+1]))
    info={'delayms': delayms,'databr':databr,'netbr':netbr,'curr_videobr':curr_videobr}
    return info


def paint(info1,info2,name):
    painting_infos = [f"rc=1 {name}:", max(info1[name]), min(info1[name]),
           round(average(info1[name]), 2), round(var(info1[name], average(info1[name])), 2)]

    painting_infos1 = [f"rc=2 {name}:", max(info2[name]), min(info2[name]),
                      round(average(info2[name]), 2), round(var(info2[name], average(info2[name])), 2)]

    #print(info1[name])
    #设置纵横坐标
    x = max(len(info1[name]), len(info2[name]))
    y = max(max(info1[name]), max(info2[name]))

    print(x,y)
    print(y/20)

    plt.ylim(0, y*1.1)
    plt.xlim(0, x*1.1)

    #
    plt.text(45, y*1.1+y/20, painting_infos, fontsize=10, color='black')
    plt.text(45, y*1.1+y/20*2, painting_infos1, fontsize=10, color='black')

    #示例
    plt.plot(info1[name], color='red', linewidth=0.3, linestyle="-", label=f"rc=1 {name}")
    plt.plot(info2[name], color='green', linewidth=0.3, linestyle="-", label=f"rc=2 {name}")
    plt.legend(loc='upper left', frameon=False)

    plt.savefig(f'f://logs/painting_{name}.png')
    plt.close()

file_info=get_info()
file_info1=get_info("f://logs/pslstreaming_log1.txt")


paint(file_info,file_info1,'delayms')
paint(file_info,file_info1,'databr')
paint(file_info,file_info1,'netbr')