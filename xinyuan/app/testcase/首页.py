# -*- coding:utf-8 -*-

import unittest
from xinyuan.app.appelement.首页 import 首页
from xinyuan.app.appelement.行情页 import 行情页
# from xinyuan.app.appelement.法币页 import 法币页
import xinyuan.app.testcase.device as device
import xinyuan.app.testcase.user_functions as func
from appium import webdriver
from time import sleep
import re
import xinyuan.app.data.account_data as account_data


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.desired_caps = device.Device.caps
        self.driver = webdriver.Remote(f"http://localhost:4723/wd/hub", self.desired_caps)
        sleep(10)
        func.验证是否登录(self.driver, account_data.kyc账号['account'], account_data.kyc账号['pwd'])
        self.page = 首页(self.driver)
        sleep(2)

    def tearDown(self):
        # self.driver.quit()
        print('over')

    def test_001_验证首页55Social跳转正确(self):
        page = self.page
        for 按钮 in [page.广场按钮(), page.群组按钮(), page.好友按钮()]:
            按钮.click()
            self.driver.implicitly_wait(10)
            self.assertEqual('55Social', page.首页_标题().text, '跳转的页面标题不正确')
            page.首页_h5网页关闭按钮().click()
            sleep(3)
            self.assertIsNotNone(按钮, '网页关闭不正确')

    def test_002_验证首页滚动公告跳转正确(self):
        self.page.首页_滚动公告().click()
        self.driver.implicitly_wait(10)
        self.assertEqual('公告', self.page.首页_标题().text, '跳转的页面标题不正确')
        self.page.首页_h5网页关闭按钮().click()
        sleep(3)
        self.assertIsNotNone(self.page.首页_滚动公告(), '网页关闭不正确')

    def test_003_验证首页标题币种跳转正确(self):
        币种名称 = self.page.首页_左边币种名称().text
        self.page.首页_左边币种名称().click()
        self.driver.implicitly_wait(10)
        hangqing_page = 行情页(self.driver)
        self.assertEqual(币种名称, hangqing_page.行情详情_标题().text, '跳转的页面标题不正确')
        self.assertIsNotNone(hangqing_page.行情详情_买入按钮(), '行情页买入功能存在')
        hangqing_page.行情详情_返回按钮().click()
        sleep(3)
        self.assertIsNotNone(self.page.首页_左边币种名称(), '网页关闭不正确')

    def test_004_验证首页公告中心和帮助中心跳转正确(self):
        func.向下滑动(self.driver, '左', 150)
        elements = {'帮助': self.page.首页_帮助中心(), '公告': self.page.首页_公告中心()}
        for key, value in elements.items():
            value.click()
            self.driver.implicitly_wait(10)
            self.assertEqual(key, self.page.首页_标题().text, '跳转的页面标题不正确')
            self.page.首页_h5网页关闭按钮().click()
            sleep(3)
            self.assertIsNotNone(value, '网页关闭不正确')

    def test_005_验证首页法币交易跳转正确(self):
        func.向下滑动(self.driver, '左', 150)
        self.page.首页_法币交易().click()
        self.driver.implicitly_wait(5)
        页面资源 = self.driver.page_source
        self.assertIn('我要买', 页面资源, '法币页跳转正确')
        self.assertIn('我要卖', 页面资源, '法币页跳转正确')

    def test_006_验证涨跌幅榜点击正确(self):
        页面资源 = self.driver.page_source
        isswipe = ('涨幅榜' in 页面资源) and ('外汇' in 页面资源)
        while not isswipe:
            func.向下滑动(self.driver, '右侧')
            页面资源 = self.driver.page_source
            isswipe = ('涨幅榜' in 页面资源) and ('外汇' in 页面资源)
        hangqing_page = 行情页(self.driver)
        for 页签 in ['涨幅榜', '跌幅榜', '成交额榜']:
            self.page.选择页签(页签).click()
            self.driver.implicitly_wait(2)
            币种名称 = self.page.首页_币种名称()[0].text
            币种计价方式 = self.page.首页_币种计价方式()[0].text
            self.page.首页_币种名称()[0].click()
            self.driver.implicitly_wait(5)
            if '暂停交易' in self.driver.page_source:
                self.driver.back()
            else:
                self.assertEqual(币种名称 + 币种计价方式, hangqing_page.行情详情_标题().text, '跳转的页面标题不正确')
                self.assertIsNotNone(hangqing_page.行情详情_买入按钮(), '行情页买入功能存在')
                hangqing_page.行情详情_返回按钮().click()
            sleep(3)
            self.assertIsNotNone(self.page.首页_币种名称, '从行情页返回正确')

    def test_007_验证外汇潮牌点击正确(self):
        页面资源 = self.driver.page_source
        isswipe = ('更多' in 页面资源) and ('外汇' in 页面资源)
        while not isswipe:
            func.向下滑动(self.driver, '右侧')
            页面资源 = self.driver.page_source
            isswipe = ('更多' in 页面资源) and ('外汇' in 页面资源)
        hangqing_page = 行情页(self.driver)
        for 页签 in ['外汇', '潮牌']:
            self.page.选择页签(页签).click()
            self.driver.implicitly_wait(2)
            币种名称 = self.page.首页_外汇币种名称()[-1].text
            # 币种计价方式 = self.page.首页_币种计价方式()[-1].text
            self.page.首页_币种名称()[-1].click()
            self.driver.implicitly_wait(5)
            print(self.driver.page_source)
            if '暂停交易' in self.driver.page_source:
                self.driver.back()
            else:
                self.assertEqual(币种名称, hangqing_page.行情详情_标题().text, '跳转的页面标题不正确')
                self.assertIsNotNone(hangqing_page.行情详情_买入按钮(), '行情页买入功能存在')
                hangqing_page.行情详情_返回按钮().click()
            sleep(3)
            self.assertIsNotNone(self.page.首页_币种名称, '从行情页返回正确')