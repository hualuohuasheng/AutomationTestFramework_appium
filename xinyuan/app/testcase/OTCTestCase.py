# -*- coding:utf-8 -*-

import unittest
from xinyuan.app.appelement.法币页 import 法币页
import xinyuan.app.testcase.device as device
import xinyuan.app.testcase.user_functions as func
from appium import webdriver
from time import sleep
import time
import xinyuan.app.data.account_data as account_data


class OTCTest(unittest.TestCase):

    def setUp(self):
        self.desired_caps = device.Device.caps
        self.driver = webdriver.Remote(f"http://localhost:4723/wd/hub", self.desired_caps)
        sleep(10)
        func.验证是否登录(self.driver, account_data.kyc账号['account'], account_data.kyc账号['pwd'])
        self.page = 法币页(self.driver)
        self.page.法币页按钮().click()
        sleep(2)

    def tearDown(self):
        # self.driver.quit()
        print('over')

    def test_001_验证法币页下单买入功能正确(self):
        res = func.获取买币页的广告数据(self.driver)
        print(res)

        page = self.page
        page.法币页广告_购买出售按钮()[1].click()
        page.下单页_买卖币种().text
        price = page.下单页_单价().text
        page.locate_by_textview_name('按交易额').click()
        page.下单页_数量或交易额编辑框().send_keys('10')
        totalmoney = page.下单页_交易总额().text
        self.assertAlmostEqual(float(totalmoney), float(price)*float('10'), delta=0.000001)
        page.下单页_交易密码().send_keys('123456')
        page.下单页_立即下单按钮().click()