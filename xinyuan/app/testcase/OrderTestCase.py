# -*- coding:utf-8 -*-

import unittest
from xinyuan.app.appelement.user import UserPage
from xinyuan.app.appelement.币币页 import 币币页
import xinyuan.app.testcase.device as device
import xinyuan.app.testcase.user_functions as func
from appium import webdriver
from time import sleep
import time
import xinyuan.app.data.account_data as account_data


class OrderTest(unittest.TestCase):

    def setUp(self):
        self.desired_caps = device.Device.caps
        self.driver = webdriver.Remote(f"http://localhost:4723/wd/hub", self.desired_caps)
        sleep(10)
        func.验证是否登录(self.driver, account_data.kyc账号['account'], account_data.kyc账号['pwd'])
        self.page = 币币页(self.driver)
        self.page.币币页按钮().click()
        sleep(2)
        self.coins = 'eth/usdt'
        func.选择币种(self.driver, self.coins)  # 选择币种
        self.driver.implicitly_wait(10)

    def tearDown(self):
        # self.driver.quit()
        print('over')

    def test_001_验证币币页下单买入功能正确(self):
        expected_result = {'币种': self.coins.upper(), '属性': '买入', '价格': '500', '数量': '0.1'}
        amount_befor_order, ordertime = func.下单(self.driver, expected_result['价格'], expected_result['数量'], '买入')
        sleep(5)
        amount_after_order = self.page.币种可用数量显示().text
        expected_result['时间'] = ordertime.split('T')[1].split('+')[0]
        expected_result['日期'] = ordertime.split('T')[0]
        func.验证下单前后数量显示是否正确(self, amount_befor_order, amount_after_order, expected_result)
        real_res = func.获取下单后当前委托数据(self.driver)
        self.assertIn(expected_result, real_res, '买入单不在当前委托列表中')

    def test_002_验证币币页下单卖出功能正确(self):
        expected_result = {'币种': self.coins.upper(), '属性': '卖出', '价格': '500', '数量': '0.1'}
        amount_befor_order, ordertime = func.下单(self.driver, expected_result['价格'], expected_result['数量'], '卖出')
        sleep(5)
        amount_after_order = self.page.币种可用数量显示().text
        expected_result['时间'] = ordertime.split('T')[1].split('+')[0]
        expected_result['日期'] = ordertime.split('T')[0]
        func.验证下单前后数量显示是否正确(self, amount_befor_order, amount_after_order, expected_result)
        real_res = func.获取下单后当前委托数据(self.driver)
        self.assertIn(expected_result, real_res, '卖出单不在当前委托列表中')

    def test_003_验证币币页当前委托订单_取消订单(self):
        res = func.获取下单后当前委托数据(self.driver)
        if len(res) == 0:
            size = self.driver.get_window_size()
            self.driver.swipe(size['width'] - 100, size['height'] / 5, size['width'] - 100, size['height'] * 4 / 5,
                              duration=500)
            func.选择币种(self.driver, 'eth/usdt')  # 选择币种
            self.driver.implicitly_wait(10)
            order = {'币种': self.coins.upper(), '属性': '卖出', '价格': '500', '数量': '0.1'}
            old_amount, ordertime = func.下单(self.driver, order['价格'], order['数量'], '卖出')
            res = func.获取下单后当前委托数据(self.driver)
        for r in res:
            self.page.获取当前委托所有订单取消()[0].click()
            self.driver.implicitly_wait(10)
            self.assertNotIn(r, func.获取下单后当前委托数据(self.driver), '订单取消后页面显示不对')

    def test_004_验证币币页下单_全部成交(self):
        for i in ['买入', '卖出']:
            price_index = 3
            if i == '卖出':
                self.page.卖出标签按钮().click()
                sleep(2)
                price_index = 6
            price_list = func.获取盘口所有数据(self.page.获取盘口所有价格())
            price = price_list[price_index]
            amount_befor_order, order_time = func.下单(self.driver, str(price), '0.01', i)
            amount_after_order = self.page.币种可用数量显示().text
            expected = {'币种': self.coins.upper(), '属性': i, '数量': '0.01', '价格': price,
                        '时间戳': time.mktime(time.strptime(order_time.split('+')[0], "%Y-%m-%dT%H:%M:%S")), '状态': '已完成'}
            sleep(10)
            history_order = func.获取下单后历史委托数据(self.driver)
            func.验证下单前后数量显示是否正确(self, amount_befor_order, amount_after_order, expected)
            func.验证委托数据和预期结果一致(self, expected, history_order)

    def test_005_验证币币页下单_分步成交_订单完成(self):
        for i in ['买入', '卖出']:
            price_index = 3
            if i == '卖出':
                self.page.卖出标签按钮().click()
                sleep(2)
                price_index = 6
            price_list = func.获取盘口所有数据(self.page.获取盘口所有价格())
            amount = 5
            price = price_list[price_index]
            amount_befor_order, order_time = func.下单(self.driver, str(price), str(amount), i)
            amount_after_order = self.page.币种可用数量显示().text
            expected = {'币种': self.coins.upper(), '属性': i, '数量': str(amount), '价格': price,
                        '时间戳': time.mktime(time.strptime(order_time.split('+')[0], "%Y-%m-%dT%H:%M:%S")), '状态': '已完成'}
            sleep(2)
            size = self.driver.get_window_size()
            func.滑动页面(self.driver, size['width'] - 100, size['height'] * 4 / 5, size['width'] - 100, size['height'] / 5,
                      duration=500)
            res_amount = []
            while '暂无数据' not in self.driver.page_source:
                cur_amount = self.page.获取当前委托所有订单数量()[0].text
                print(cur_amount)
                res_amount.append(float(cur_amount))
                self.assertTrue(float(cur_amount) < float(expected['数量']), '123')
                sleep(5)
                if len(self.page.获取当前委托所有订单数量()) == 0:
                    break
            self.assertTrue(len(res_amount) > 0, '分步成交过程中成交次数不对')
            history_order = func.获取下单后历史委托数据(self.driver)
            func.验证下单前后数量显示是否正确(self, amount_befor_order, amount_after_order, expected)
            func.验证委托数据和预期结果一致(self, expected, history_order)
            self.assertFalse('取消' in self.driver.page_source, '订单完成后当前委托中应该没有订单')
            func.滑动页面(self.driver, size['width'] - 100, size['height'] * 4 / 5, size['width'] - 100, size['height'] / 5,
                      duration=500)

    def test_006_验证币币页下单_分步成交_订单未完成(self):
        for i in ['买入', '卖出']:
            price_index = 0
            if i == '卖出':
                self.page.卖出标签按钮().click()
                sleep(2)
                price_index = 5
            price_list = func.获取盘口所有数据(self.page.获取盘口所有价格())
            amount = 10
            price = price_list[price_index]
            amount_befor_order, order_time = func.下单(self.driver, str(price), str(amount), i)
            sleep(2)
            size = self.driver.get_window_size()
            func.滑动页面(self.driver, size['width'] - 100, size['height'] * 4 / 5, size['width'] - 100, size['height'] / 5,
                      500)
            res_amount = []
            while '暂无数据' not in self.driver.page_source:
                cur_amount = self.page.获取当前委托所有订单数量()[0].text
                print(cur_amount)
                res_amount.append(float(cur_amount))
                self.assertTrue(float(cur_amount) < amount, '123')
                sleep(5)
                if float(cur_amount) < amount:
                    self.page.获取当前委托所有订单取消()[0].click()
                    break
                sleep(2)
            func.滑动页面(self.driver, size['width'] - 100, size['height'] / 5, size['width'] - 100, size['height'] * 4 / 5,
                      500)
            amount_after_order = self.page.币种可用数量显示().text
            self.assertEqual(len(res_amount), 1, '分步成交过程中成交次数不对')
            history_res = func.获取下单后历史委托数据(self.driver, False)
            expected = {'币种': self.coins.upper(), '属性': i, '数量': history_res['数量'], '价格': price,
                        '时间戳': time.mktime(time.strptime(order_time.split('+')[0], "%Y-%m-%dT%H:%M:%S")), '状态': '已撤单'}
            func.验证下单前后数量显示是否正确(self, amount_befor_order, amount_after_order, expected)
            func.验证委托数据和预期结果一致(self, expected, history_res)

    def test_007_验证币币页下单_历史委托_筛选(self):
        self.page.右上更多功能按钮().click()
        self.driver.implicitly_wait(3)
        self.page.历史委托按钮().click()
        self.driver.implicitly_wait(5)
        时间 = {'1天': 1, '1周': 7, '1月': 30, '全部': 0}
        for key in 时间.keys():
            func.历史委托中筛选(self.driver, [[key, 0]])
            if key != '全部':
                func.验证历史委托中按时间筛选正确(self, self.page.获取当前委托所有订单日期()[-1].text, 时间[key])

        func.历史委托中筛选(self.driver, [['已完成', 0]])
        func.历史委托中筛选(self.driver, [['已取消', 0]])

