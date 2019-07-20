# -*- coding:utf-8 -*-

import unittest
from xinyuan.app.appelement.资产页 import 资产页
import xinyuan.app.testcase.device as device
import xinyuan.app.testcase.user_functions as func
from appium import webdriver
from time import sleep, strftime, strptime
import re
import xinyuan.app.data.account_data as account_data


class CurrencyTest(unittest.TestCase):

    def setUp(self):
        self.desired_caps = device.Device.caps
        self.driver = webdriver.Remote(f"http://localhost:4723/wd/hub", self.desired_caps)
        sleep(10)
        func.验证是否登录(self.driver, account_data.kyc账号['account'], account_data.kyc账号['pwd'])
        self.page = 资产页(self.driver)
        self.page.资产页按钮().click()
        sleep(2)

    def tearDown(self):
        # self.driver.quit()
        print('over')

    def test_001_验证资产页资产汇总显示正确(self):
        page = self.page
        for ele in [page.资产页_币币账户按钮(), page.资产页_法币账户按钮()]:
            ele.click()
            self.driver.implicitly_wait(5)
            资产合计 = func.获取资产页资产统计数据(self.driver)
            print(资产合计)
            self.assertEqual(1, len(re.findall(r'\d+.\d{2}', 资产合计['合计'])), '合计资产显示正确')
            self.assertEqual(1, len(re.findall(r'\d+.\d{4}', 资产合计['换算'])), '换算资产显示正确')

    def test_002_验证资产页隐藏显示资产功能正确(self):
        page = self.page
        for ele in [page.资产页_币币账户按钮(), page.资产页_法币账户按钮()]:
            ele.click()
            self.driver.implicitly_wait(5)
            原始资产合计 = func.获取资产页资产统计数据(self.driver)
            原始币种数据 = func.获取资产页各币种资产数据(self.driver)
            page.资产页_资产汇总_隐藏显示资产按钮().click()
            sleep(0.5)
            隐藏资产合计 = func.获取资产页资产统计数据(self.driver)
            隐藏币种数据 = func.获取资产页各币种资产数据(self.driver)
            inum = 4 if page.is_android else 6
            self.assertEqual("*" * inum, 隐藏资产合计['合计'], '隐藏资产显示不正确')
            self.assertEqual("*" * inum, 隐藏资产合计['换算'], '隐藏资产显示不正确')
            for info in 隐藏币种数据:
                self.assertEqual("*" * inum, info['数量'], '隐藏资产显示不正确')
                self.assertEqual("*" * inum, info['换算数量'], '隐藏资产显示不正确')
            page.资产页_资产汇总_隐藏显示资产按钮().click()
            sleep(0.5)
            self.assertEqual(原始资产合计, func.获取资产页资产统计数据(self.driver), '隐私显示资产后资产显示不正确')
            self.assertEqual(原始币种数据, func.获取资产页各币种资产数据(self.driver), '隐私显示资产后资产显示不正确')

    def test_003_验证资产页搜索币种功能正确(self):
        page = self.page
        不存在的币种 = 'gg'
        搜索币种名称 = ['usdt', 'eos', 'ff', 'btc', 'eth', 'usdd'] + [不存在的币种]
        法币币种 = ['usdd', 'usdt', 'btc', 'eth']
        页签按钮 = [page.资产页_币币账户按钮(), page.资产页_法币账户按钮()]
        for ele in 页签按钮:
            ele.click()
            self.driver.implicitly_wait(5)
            币种数据 = func.获取资产页各币种资产数据(self.driver)
            page.资产页_币种资产_搜索按钮().click()
            sleep(0.5)
            for 币种 in 搜索币种名称:
                page.资产页_币种资产_搜索编辑框().send_keys(币种)
                搜索币种数据 = func.获取资产页各币种资产数据(self.driver)
                if (币种 not in 法币币种 and 页签按钮.index(ele) == 1) or (不存在的币种 in 币种):
                    self.assertEqual([], 搜索币种数据, '币种不存在时搜索结果为空')
                else:
                    self.assertEqual(币种.upper(), 搜索币种数据[0]['币种名称'], '搜索币种结果不正确')
            page.资产页_币种资产_搜索取消按钮().click()
            self.driver.implicitly_wait(3)
            self.assertEqual(币种数据, func.获取资产页各币种资产数据(self.driver), '取消搜索后币种数据显示正确')

    def test_004_验证资产页币币账户币种的资产细节页面(self):
        page = self.page
        page.资产页_币币账户按钮().click()
        self.driver.implicitly_wait(5)
        func.资产页搜索币种(self.driver, 'eth')
        币种数据 = func.获取资产页各币种资产数据(self.driver)[0]
        page.资产页_币种资产_币种名称()[0].click()
        self.driver.implicitly_wait(5)
        总额 = float(page.资产页_资产细节_总额().text)
        可用余额 = float(page.资产页_资产细节_可用余额().text)
        下单冻结 = float(page.资产页_资产细节_下单冻结().text)
        self.assertAlmostEqual(总额, 可用余额+下单冻结, delta=0.001, msg='币种资产计算不正确')
        self.assertEqual(币种数据['币种名称'], page.资产页_资产细节_币种名称().text, '币种名称显示不正确')
        self.assertEqual(币种数据['币种详细名称'], page.资产页_资产细节_币种计价方式().text, '币种名称显示不正确')

        res = [page.资产页_资产细节_总额().text, page.资产页_资产细节_可用余额().text, page.资产页_资产细节_下单冻结().text,
               page.资产页_资产细节_币种名称().text, page.资产页_资产细节_币种计价方式().text, page.资产页_资产细节_充值按钮(),
               page.资产页_资产细节_提现按钮()]

        print(res)

    def test_005_验证资产页_充值提现(self):
        data = {'币种': 'eth', '提现数量': '5.2'}
        page = self.page
        page.资产页_币币账户按钮().click()
        self.driver.implicitly_wait(5)
        func.资产页搜索币种(self.driver, data['币种'])
        币种数据 = func.获取资产页各币种资产数据(self.driver)[0]
        page.资产页_币种资产_币种名称()[0].click()
        self.driver.implicitly_wait(5)
        page.资产页_资产细节_充值按钮().click()
        self.driver.implicitly_wait(5)
        data['充值地址'] = page.充值页面_充值地址().text
        page.充值页面_复制地址按钮().click()
        self.driver.back()
        func.执行提现(self.driver, data)

    def test_006_验证资产页_划转提现(self):
        data = {'币种': 'eth', '提现数量': '5.324'}
        page = self.page
        page.资产页_法币账户按钮().click()
        self.driver.implicitly_wait(5)
        func.资产页搜索币种(self.driver, data['币种'])
        page.资产页_币种资产_币种名称()[0].click()
        self.driver.implicitly_wait(5)
        for from_account in ['币币账户', '法币账户']:
            划转前数量 = func.获取划转页面账户数量(self.driver)
            func.划转提现(self.driver, data['提现数量'], from_account)
            划转后数量 = func.获取划转页面账户数量(self.driver)
            print(划转前数量, 划转后数量)
            func.验证划转提现功能正确(self, 划转前数量, 划转后数量, data['提现数量'], from_account)
            # 验证记录
        self.driver.back()

    def test_007_验证资产页_隐藏小额资产(self):
        page = self.page
        页签按钮 = [page.资产页_币币账户按钮(), page.资产页_法币账户按钮()]
        for ele in 页签按钮:
            ele.click()
            self.driver.implicitly_wait(5)
            隐藏前页面 = self.driver.page_source
            page.资产页_币种资产_勾选隐藏小额资产按钮().click()
            币种资产 = func.获取资产页各币种资产数据(self.driver)
            if page.is_android:
                self.assertEqual(len(币种资产), 0)
            page.资产页_币种资产_勾选隐藏小额资产按钮().click()
            sleep(0.5)
            隐藏后页面 = self.driver.page_source
            self.assertEqual(隐藏前页面, 隐藏后页面)
