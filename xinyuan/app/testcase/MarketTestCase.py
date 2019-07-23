# -*- coding:utf-8 -*-

import unittest
from xinyuan.app.appelement.行情页 import 行情页
from xinyuan.app.appelement.币币页 import 币币页
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

    def test_001_验证行情页自选通证添加正确(self):
        self.page.编辑通证按钮().click()
        self.driver.implicitly_wait(5)
        self.page.编辑通证_添加按钮().click()
        self.driver.implicitly_wait(5)
        搜索交易对 = 'eth/usdt'
        func.行情页添加自选通证(self.driver, 搜索交易对)
        res = func.获取行情页编辑自选通证页的数据(self.driver)
        self.assertIn(搜索交易对.upper(), res, '自选通证添加正确')
        self.page.编辑通证_完成按钮().click()
        自选通证页数据 = func.获取行情页币种交易对数据(self.driver)
        交易对数据 = [value['币种交易对'] for value in 自选通证页数据]
        self.assertIn(搜索交易对.upper(), 交易对数据, '自选通证页数据显示症')

    def test_002_验证行情页自选通证删除正确(self):
        self.page.编辑通证按钮().click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_ios_class_chain()
        self.driver.find_element_by_ios_predicate()
        搜索交易对 = ['eth/usdt', 'btc/usdt', 'eos/btc']
        for i in 搜索交易对:
            func.行情页添加自选通证(self.driver, i)
        res = func.获取行情页编辑自选通证页的数据(self.driver)
        print(res.index(搜索交易对[1].upper()))
        self.page.编辑通证_全选按钮().click()
        self.page.编辑通证_删除按钮().click()
        sleep(0.5)
        self.page.选择页签('确定').click()
        res = func.获取行情页编辑自选通证页的数据(self.driver)
        self.assertEqual(len(res), 0, '全部删除功能正确')
        self.page.编辑通证_完成按钮().click()
        # print(self.driver.page_source)

    def test_002_验证行情页币种概况和详情数据一致(self):
        self.page.区块链通证按钮().click()
        self.driver.implicitly_wait(5)
        res = func.获取行情页币种交易对数据(self.driver)
        self.page.币种列表_币种名称()[0].click()
        info = {'币种交易对': self.page.行情详情_标题().text, '最新价': self.page.行情详情_市场价格().text,
                '最新价换算价格': self.page.行情详情_当前计价方式价格().text, '24H量': self.page.行情详情_24H量().text,
                '涨跌幅': self.page.行情详情_涨跌幅百分比().text}
        self.assertIn(info, res, '行情详情页面数据和行情页数据应一致')
        self.page.行情详情_返回按钮().click()
        sleep(2)

    def test_003_验证行情页币种概况和详情数据一致(self):
        币种交易对 = 'eth/usdt'
        func.行情页搜索币种(self.driver, 币种交易对)
        self.assertEqual(币种交易对.upper(), self.page.行情详情_标题().text, '搜索结果正确')

    def test_004_验证行情详情页买入卖出功能跳转正确(self):
        for 按钮 in ['买入', '卖出']:
            self.page.区块链通证按钮().click()
            self.driver.implicitly_wait(5)
            ele = self.page.币种列表_币种名称()[0]
            币种名称 = ele.text
            sleep(10)
            币种计价方式 = self.page.币种列表_币种计价方式名称()[0].text
            ele.click()
            self.driver.implicitly_wait(5)
            self.page.选择页签(按钮).click()
            sleep(1)
            bibi_page = 币币页(self.driver)
            print(币种名称, 币种计价方式)
            # self.assertEqual(币种交易对.upper(), bibi_page.币种标题显示().text, '币币页跳转不正确')
            预期计价方式 = 币种计价方式.split('/')[1] if 按钮 == '买入' else 币种名称
            self.assertEqual(预期计价方式, bibi_page.币种可用计价方式().text, '默认进入页面不正确')
            self.page.行情页按钮().click()
            sleep(2)

    def test_005_验证行情详情页添加删除自选功能正确(self):
        self.page.区块链通证按钮().click()
        self.driver.implicitly_wait(5)
        self.page.币种列表_币种名称()[0].click()
        self.driver.implicitly_wait(5)
        self.page.行情详情_自选按钮().click()
        self.assertIsNotNone(self.page.选择页签('添加自选成功'))
        sleep(2)
        self.page.行情详情_自选按钮().click()
        self.assertIsNotNone(self.page.选择页签('删除自选成功'))

    def test_006_验证行情详情页分享保存图片功能正确(self):
        self.page.区块链通证按钮().click()
        self.driver.implicitly_wait(5)
        self.page.币种列表_币种名称()[0].click()
        self.driver.implicitly_wait(5)
        self.page.行情详情_分享按钮().click()
        self.driver.implicitly_wait(3)
        self.page.行情详情_分享_保存图片按钮().click()
        sleep(0.5)
        self.assertIn('成功', self.driver.page_source, '保存图片功能正常')
