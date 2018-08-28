# -*- coding:utf-8 -*-

import os
import re
import subprocess

def get_android_app_info(app="iRoom"):
    # get device name
    # readDeviceId = os.popen("adb devices").readlines()
    # deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
    deviceId = subprocess.getoutput('adb devices').split('\n')[1].split("\t")[0]

    # get Android device systerm version
    # deviceVersion = os.popen('adb shell getprop ro.build.version.release').read()
    deviceVersion = subprocess.getoutput('adb shell getprop ro.build.version.release')

    # get app package name and activity
    if app == "iRoom":
        getappInfo = subprocess.getoutput("adb shell dumpsys window w |findstr \/|findstr name=")
        appInfo = re.findall(r'com.+?tivity', getappInfo)[0].split('/')
        appPackage = appInfo[0]
        appActivity = 'com.powerinfo.pi_iroom.demo.setting.LoginSettingActivity'
    else:
        getappInfo = subprocess.getoutput("adb shell dumpsys window w |findstr \/|findstr name=")
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
        'xcodeOrgId': 'H6E8P88Q4E',
        'xcodeSigningId': 'iPhone Develaoper',
        'noReset': 'true'
    }

    print(desired_caps)
    return desired_caps


