# -*- coding:utf-8 -*-

android_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "CSX0217629006119",
    "appPackage": "com.ex55.app",
    "appActivity": "com.ex55.view.activity.NewSplashActivity",
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

    @classmethod
    def get_cur_device(cls, device):
        cls.caps = android_caps
