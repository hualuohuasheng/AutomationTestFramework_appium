# -*- coding:utf-8 -*-

import os
from pathlib import Path
import re
import subprocess
import platform

print(platform.platform())

# 获取当前目录
# print(os.getcwd())
# print(os.path.abspath(os.path.dirname(__file__)))
# print(Path.cwd())

# 获取上级目录
print(os.name)

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


a = ['a','b','c','d','e','f','g']
print(a)

print(a[2:5+1])

filedir = "/Users/liminglei/Downloads/"
file_toogle = open(filedir+"file1.txt",'w+')
file_toogle.writelines(a[1:(5+1)])
file_toogle.close()