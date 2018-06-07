# -*- coding:utf-8 -*-

import os
import re
import platform
from appium import webdriver

def get_app_info():
    # get device name
    readDeviceId = os.popen("adb devices").readlines()
    deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]

    # get Android device systerm version
    deviceVersion = os.popen('adb shell getprop ro.build.version.release').read()

    # get app package name and activity
    getappInfo = os.popen("adb shell dumpsys window w |findstr \/|findstr name=").read()
    appInfo = re.findall(r'com.+?tivity', getappInfo)[0].split('/')

    desired_caps = {
        'platformName': 'Android',
        'platformVersion': deviceVersion.rstrip('\n'),
        'deviceName': deviceId,
        'appPackage': appInfo[0],
        'appActivity': appInfo[0] + ".setting.LoginSettingActivity",
        'autoAcceptAlerts': 'true',
        'noReset': 'true'
    }

    print(desired_caps)
    return desired_caps

desired_caps = get_app_info()

def get_system_info():

    #  get python version
    print(platform.python_version())

    print(platform.architecture())

    print(platform.node())

    print(platform.platform())

    print(platform.system())

# get_system_info()

command_executor = "http://localhost:4723/wd/hub"

driver = webdriver.Remote(command_executor, desired_caps)
