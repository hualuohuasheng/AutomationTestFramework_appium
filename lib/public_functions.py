# -*- coding:utf-8 -*-

import os
import re
import subprocess
from pathlib import Path
import yaml
import platform

def 获取当前系统():
    systeminfo = platform.platform()
    print(systeminfo)
    if 'Windows' in systeminfo :
        systemname = 'windows'
    elif 'Darwin' in systeminfo :
        systemname = 'mac'
    else:
        systemname = 'linux'
    return systemname

def 获取控件文件信息(filename='app控件'):
    控件文件路径 = Path(__file__).cwd().parent / f'{filename}.yaml'
    with open(控件文件路径,'r', encoding='gbk') as loadfile:
        info = yaml.load(loadfile)
    return info

def get_android_app_info(app="iRoom"):
    # get device name
    # readDeviceId = os.popen("adb devices").readlines()
    # deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
    deviceId = subprocess.getoutput('adb devices').split('\n')[1].split("\t")[0]

    # get Android device systerm version
    # deviceVersion = os.popen('adb shell getprop ro.build.version.release').read()
    deviceVersion = subprocess.getoutput('adb shell getprop ro.build.version.release')

    # get app package name and activity

    if 'mac' in 获取当前系统():
        find_exec = 'grep'
    else:
        find_exec = 'findstr'
    cmd_exec = f'adb shell dumpsys window w |{find_exec} \/|{find_exec} name='

    if app == "iRoom":
        getappInfo = subprocess.getoutput(cmd_exec)
        appInfo = re.findall(r'com.+?tivity', getappInfo)[0].split('/')
        appPackage = appInfo[0]
        appActivity = 'com.powerinfo.pi_iroom.demo.setting.LoginSettingActivity'
    else:
        getappInfo = subprocess.getoutput(cmd_exec)
        appInfo = re.findall(r'com.+?tivity', getappInfo)[0].split('/')
        appPackage = appInfo[0]
        appActivity = appInfo[1]
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': deviceVersion.rstrip('\n'),
        'deviceName': deviceId,
        'appPackage': appPackage,
        'appActivity': appActivity,
        'autoAcceptAlerts': 'true',
        'noReset': 'true'
    }

    print(desired_caps)
    return desired_caps

def get_ios_app_info():
    udid = os.popen('idevice_id --list').readlines()
    bundleid = os.popen("ideviceInstaller -l|grep PowerInfo").readlines()
    device_os_version = os.popen('ideviceinfo -k ProductVersion').readlines()

    desired_caps = {
        'platformName':'IOS',
        'platformVesion': device_os_version[0],
        'deviceName': 'IPhone',
        'automationName': 'XCUITest',
        'bundleId': bundleid[0].split(' - ')[0],
        'udid': udid[0].rstrip(),
        'noReset': 'true'
    }

    print(desired_caps)
    return desired_caps


