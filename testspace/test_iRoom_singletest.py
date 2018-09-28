# -*- coding:utf-8 -*-

import sys
sys.path.append('..')

from time import sleep
import unittest
import lib.public_functions as pubfuc
from appium import webdriver


desired_caps = pubfuc.get_android_app_info()

控件信息 = pubfuc.获取控件文件信息()

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)

driver.find_element_by_xpath("//android.widget.TextView[@text='多人群聊']").click()
sleep(1)

driver.find_element_by_xpath("//android.widget.TextView[@text='RoomID :2255']").click()
sleep(1)

print(driver.page_source)


driver.find_element_by_xpath("//android.widget.Button[@text='JOIN']").click()


num = 0

while num < 300:
    sleep(20)
    driver.lock(5)
    driver.unlock()
    num += 1
    print(f"第{num}次")


driver.lock(5)

driver.unlock()

sleep(5)

driver.quit()