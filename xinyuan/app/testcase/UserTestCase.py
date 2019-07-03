# -*- coding:utf-8 -*-

import unittest
import xinyuan.app.testcase.public_functions as pub_func
import xinyuan.app.testcase.device as device
from appium import webdriver


class UserTest(unittest.TestCase):

    def setUp(self):
        self.desired_caps = device.Device.caps
        print(self.desired_caps)
        self.driver = webdriver.Remote("http://localhost:/wd/hub", self.desired_caps)
        print(isinstance(self.driver, webdriver))
        pass

    def tearDown(self):
        pass

    def test_001_查看订单(self):
        print(1)
        pass