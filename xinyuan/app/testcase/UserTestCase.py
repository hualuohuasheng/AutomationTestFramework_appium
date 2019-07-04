# -*- coding:utf-8 -*-

import unittest
import xinyuan.app.testcase.public_functions as pub_func
from xinyuan.app.appelement.user import User
import xinyuan.app.testcase.device as device
# import xinyuan.app.testcase.appiumserver as appium_server
from appium import webdriver
from time import sleep


class UserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.desired_caps = device.Device.caps
        cls.driver = webdriver.Remote(f"http://localhost:4723/wd/hub", cls.desired_caps)
        sleep(10)

    def setUp(self):
        self.user = User(self.driver)
        # is_sleep = '首页' not in self.driver.page_source
        # print(is_sleep)

    def tearDown(self):
        pass

    def test_001_查看订单(self):
        print(self.driver.page_source)

    def test_002_买单(self):
        self.user.进入用户页面按钮.click()
        sleep(0.5)
        uid = self.user.uid.text
        print(uid)