# -*-coding:utf-8 -*-

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from time import sleep
# import xinyuan.app.testcase.public_functions as pub_func
import xinyuan.app.testcase.device as device

desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "CSX0217629006119",
    "appPackage": "com.ex55.app",
    "appActivity": "com.ex55.view.activity.NewSplashActivity",
    "noReset": "true",
    "newCommandeTimeOut": 3600
}
#
# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# sleep(10)
#
# print(driver.page_source)


if __name__ == '__main__':

    # device_id = '69DDU17209002446'
    # device = device.Device.get_cur_device(device_id, '8.0')
    device_id = '63d592bb3ebf4f406f36c4aab99b5988a32d2318'
    dev = device.Device.get_cur_device(device_id, '12.3.1', 'IOS')

    driver = webdriver.Remote("http://localhost:4723/wd/hub", device.Device.caps)
    driver.find_element(MobileBy.ACCESSIBILITY_ID, '行情').click()
    sleep(1)
    locat_str = "type == 'XCUIElementTypeStaticText' and name == '区块链通证'"
    ele = driver.find_element(MobileBy.IOS_PREDICATE, locat_str)
    print(ele)
    print(driver.find_element(MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "区块链通证"`]'))
    # XCUIElementTypeScrollView[1]/XCUIElementTypeOther[3]
    driver.find_element(MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[4]').click()
    sleep(10)
    driver.quit()