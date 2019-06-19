# -*-coding:utf-8 -*-

from appium import webdriver
from time import sleep

desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "CSX0217629006119",
    "appPackage": "com.ex55.app",
    "appActivity": "com.ex55.view.activity.NewSplashActivity",
    "noReset": "true",
    "newCommandeTimeOut": 3600
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
sleep(10)

print(driver.page_source)