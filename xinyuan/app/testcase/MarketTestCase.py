# -*- coding:utf-8 -*-

import unittest
from xinyuan.app.appelement.行情页 import 行情页
import xinyuan.app.testcase.device as device
import xinyuan.app.testcase.user_functions as func
from appium import webdriver
from time import sleep
import time
import xinyuan.app.data.account_data as account_data


class MarketTest(unittest.TestCase):

    def setUp(self):
        self.desired_caps = device.Device.caps
        self.driver = webdriver.Remote(f"http://localhost:4723/wd/hub", self.desired_caps)
        sleep(10)
        func.验证是否登录(self.driver, account_data.kyc账号['account'], account_data.kyc账号['pwd'])
        self.page = 行情页(self.driver)
        self.page.行情页按钮().click()
        sleep(2)

    def tearDown(self):
        # self.driver.quit()
        print('over')

    def test_001_验证行情页正确(self):
        self.page.编辑通证按钮().click()
        self.driver.implicitly_wait(5)
        self.page.编辑通证_添加按钮().click()
        self.driver.implicitly_wait(5)
        搜索交易对 = 'eth/usdt'
        self.page.行情页搜索_币种编辑框().send_keys(搜索交易对)
        self.page.编辑通证_勾选自选按钮().click()
        self.page.行情页搜索_取消按钮().click()
        self.driver.implicitly_wait(2)
        res = func.获取行情页编辑自选通证页的数据(self.driver)
        self.assertIn(搜索交易对.upper(), res, '自选通证添加正确')
        self.page.编辑通证_完成按钮().click()
        自选通证页数据 = func.获取资产页各币种资产数据(self.driver)
        交易对数据 = [value['币种']+ value['计价名称'] for key, value in 自选通证页数据.items()]
        self.assertIn(res, 交易对数据, '自选通证页数据显示症')
