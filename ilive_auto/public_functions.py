import os
import re

def get_android_app_info(app="iLive"):
    # get device name
    readDeviceId = os.popen("adb devices").readlines()
    deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]

    # get Android device systerm version
    deviceVersion = os.popen('adb shell getprop ro.build.version.release').read()

    # get app package name and activity
    if app == "iLive":
        appPackage = 'com.powerinfo.pi_iroom.demo'
        appActivity = 'com.powerinfo.pi_iroom.demo.setting.LoginSettingActivity'
    else:
        getappInfo = os.popen("adb shell dumpsys window w |findstr \/|findstr name=").read()
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

info = get_android_app_info()