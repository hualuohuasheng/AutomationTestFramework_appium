# -*- coding:utf-8 -*-
import os
from pathlib import Path
import re
import subprocess

# 获取当前目录
# print(os.getcwd())
# print(os.path.abspath(os.path.dirname(__file__)))
# print(Path.cwd())

# 获取上级目录

# print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
# print(os.path.abspath(os.path.dirname(os.getcwd())))
# print(os.path.abspath(os.path.join(os.getcwd(),'..')))

fn = Path(__file__)
print(fn.name)
print(fn.suffix)
print(fn.stem)

print(Path(__file__).cwd().parent)

p = subprocess.getoutput('adb devices')

print(p.split('\n')[1].split("\t")[0])

import sys
print(dir(__file__))




