# -*- coding:utf-8 -*-

android_caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "platformVersion": "9",
    "deviceName": "CSX0217629006119",
    "appPackage": "com.ex55.app",
    "appActivity": "com.ex55.view.activity.NewSplashActivity",
    "appWaitActivity": "com.ex55.view.activity.GalaxyMainActivity",
    "noReset": "true",
    "autoAcceptAlerts": "true",
    "newCommandTimeout": 3600
}

ios_caps = {
    "platformName": "IOS",
    "platformVersion": "11.2.6",
    "udid": "",
    "deviceName": "IPhone",
    "automationName": "XCUITest",
    "bundleId": "com.55.globalmarkets",
    "noReset": "true",
    "autoAcceptAlerts": "true",
    "newCommandTimeout": 3600,
    "waitForQuiescence": "false"
}


class Device:

    caps = None

    @classmethod
    def get_cur_device(cls, device_id, version, platform='Android'):
        cls.caps = android_caps if 'Android' in platform else ios_caps
        cls.caps['platformName'] = platform
        cls.caps['platformVersion'] = version
        if 'IOS' in platform:
            cls.caps['udid'] = device_id
        else:
            cls.caps['deviceName'] = device_id
