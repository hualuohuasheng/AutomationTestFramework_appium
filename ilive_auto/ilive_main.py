# -*- coding:utf-8 -*-

import os
import re
from time import sleep
from appium import webdriver

class AndriodILive:

    def __init__(self,desired_caps,command_executor="http://localhost:4723/wd/hub"):
        self.driver = webdriver.Remote(command_executor, desired_caps)

    def 创建房间(self):
        self.driver.find_element_by_id("com.powerinfo.pi_iroom.demo:id/iv_create_room").click()
        sleep(1)
        self.driver.find_element_by_xpath("//android.widget.Button[@text='START']").click()

    def 退出房间(self):
        self.driver.find_element_by_id("com.powerinfo.pi_iroom.demo:id/iv_back").click()


