# -*- coding:utf-8 -*-

import unittest
from xinyuan.app.appelement.user import UserPage
from xinyuan.app.appelement.币币页 import 币币页
import xinyuan.app.testcase.device as device
import xinyuan.app.testcase.user_functions as func
from appium import webdriver
from time import sleep
import xinyuan.app.data.account_data as account_data


class OrderTest(unittest.TestCase):

    def setUp(self):
        self.desired_caps = device.Device.caps
        self.driver = webdriver.Remote(f"http://localhost:4723/wd/hub", self.desired_caps)
        sleep(10)
        func.验证是否登录(self.driver, account_data.kyc账号['account'], account_data.kyc账号['pwd'])

    def tearDown(self):
        # self.driver.quit()
        print('over')

    def test_001_验证币币页下单买入功能正确(self):
        page = 币币页(self.driver)
        page.币币页按钮().click()
        sleep(2)
        coins = 'eth/usdt'
        func.选择币种(self.driver, coins)   #   选择币种
        old_amount = func.下单(self.driver, '500', '0.1')
        sleep(10)
        new_amount = page.币种可用数量显示().text
        # 验证下单前后数量是否一致
        self.assertEqual(float(old_amount)-50, float(new_amount), '下单前后数量不一致')
        # print(page.币种可用数量显示().text)
        size = self.driver.get_window_size()
        self.driver.swipe(size['width'] - 100, size['height'] * 4 / 5, size['width'] - 100, size['height'] / 5,
                          duration=500)
        elements = page.获取当前委托所有订单币种()
        for e in elements:
            print(e.text)
        for e in page.获取当前委托所有订单数量():
            print(e.text)
        for e in page.获取当前委托所有订单价格():
            print(e.text)
        for e in page.获取当前委托所有订单时间():
            print(e.text)

    def test_002_验证币币页下单卖出功能正确(self):
            page = 币币页(self.driver)
            page.币币页按钮().click()
            sleep(2)
            coins = 'eth/usdt'
            func.选择币种(self.driver, coins)  # 选择币种
            sleep(5)
            expected_result = {'币种': coins, '价格': '500', '数量': '0.2'}
            old_amount = func.下单(self.driver, expected_result['价格'], expected_result['数量'], '卖出')
            sleep(10)
            new_amount = page.币种可用数量显示().text
            # 验证下单前后数量是否一致
            self.assertEqual(float(old_amount) - 0.1, float(new_amount), '下单前后数量不一致')
            func.验证下单后当前委托显示正确(self.driver, expected_result)

    def test_003_验证币币页当前委托(self):
        page = 币币页(self.driver)
        page.币币页按钮().click()
        sleep(2)
        page.卖出标签按钮().click()
        sleep(3)
        size = self.driver.get_window_size()
        self.driver.swipe(size['width'] - 100, size['height'] * 4 / 5, size['width'] - 100, size['height'] / 5,
                          duration=500)
        # elements = page.获取当前委托所有订单币种()
        for e in page.获取当前委托所有订单币种():
            print(e.text)
        for e in page.获取当前委托所有订单数量():
            print(e.text)
        for e in page.获取当前委托所有订单价格():
            print(e.text)
        for e in page.获取当前委托所有订单时间():
            print(e.text)