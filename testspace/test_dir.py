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
print(p)
print(p.split('\n')[1].split("\t")[0])
print(re.findall(r'^\w*\b', p.split('\n')[1])[0])

import sys

sys.path.append("..")

from lib.public_functions import get_android_app_info
# import lib.public_functions as f

info = get_android_app_info('liveme')

print(info)




