# -*- coding:utf-8 -*-

import os
from pathlib import Path
import re
import subprocess
import platform

# print(platform.platform())

# 获取当前目录
# print(os.getcwd())
# print(os.path.abspath(os.path.dirname(__file__)))
# print(Path.cwd())

# 获取上级目录
# print(os.name)

# print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
# print(os.path.abspath(os.path.dirname(os.getcwd())))
# print(os.path.abspath(os.path.join(os.getcwd(),'..')))

fn = Path(__file__)
print(fn.name)
print(fn.suffix)
print(fn.stem)

print(Path(__file__).cwd().parent)

# p = subprocess.getoutput('adb devices')
# print(p)
# print(p.split('\n')[1].split("\t")[0])
# print(re.findall(r'^\w*\b', p.split('\n')[1])[0])

# import sys

# sys.path.append("..")

# from lib.public_functions import get_android_app_info
# import lib.public_functions as f

# info = get_android_app_info('liveme')

# print(info)

filepath = Path(__file__).cwd().parent / 'app控件.yml'

print(filepath)

import yaml

with open(filepath, 'r', encoding='gbk') as fs:
    info = yaml.load(fs)

print(info)
print(info['liveme']['开播'])

# from multiprocessing import Process,Pool
# import subprocess
# import time
#
# def startAppiumServer(aport,bport,udid):
#     print()
#     cmd_base = "node /Applications/Appium.app/Contents/Resources/app/node_modules/appium/build/lib/main.js -a 127.0.0.1 --local-timezone"
#     cmd = cmd_base + f" -p {aport}"+ f" -bp {bport}"+ f" -U {udid} > /Users/liminglei/Desktop/appium/appiumlog.txt"
#     subprocess.Popen(cmd,shell=True)
#
#
# proc = Process(target=startAppiumServer,args=(4723,4724,"VGT7N17811000107",))
#
# proc.start()
# proc.join()
# # time.sleep(15)
# proc.terminate()



import logging

