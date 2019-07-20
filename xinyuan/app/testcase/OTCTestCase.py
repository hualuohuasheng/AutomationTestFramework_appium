# -*- coding:utf-8 -*-

import unittest
from xinyuan.app.appelement.法币页 import 法币页
import xinyuan.app.testcase.device as device
import xinyuan.app.testcase.user_functions as func
from appium import webdriver
from time import sleep, strftime, strptime
import re
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

    def test_001_验证法币页购买售出页面显示(self):
        page = self.page
        page.选择法币币种页签('我要买').click()
        self.driver.implicitly_wait(5)
        page.选择法币币种页签('USDT').click()
        self.driver.implicitly_wait(5)
        res = func.获取法币页广告数据(self.driver)
        广告详情 = res[1]
        print(res[1])
        #  法币下单
        page.法币页广告_购买出售按钮()[1].click()
        self.driver.implicitly_wait(5)
        price = page.下单页_单价().text
        self.assertEqual(price.split(' ')[1], 广告详情['单价'].split(" ")[1], '单价的单位不一致')
        self.assertAlmostEqual(float(price.split(' ')[0]), float(广告详情['单价'].split(" ")[0]), delta=0.01)
        page.选择页签('按交易额').click()
        self.assertEqual(f"限额 {广告详情['最小限额']} - {广告详情['最大限额'].split(' ')[0]}", page.下单页_数量或交易额编辑框().text)
        交易总额 = '123.4'
        page.下单页_数量或交易额编辑框().send_keys(交易总额)
        total_money = page.下单页_交易总额().text
        数量 = page.下单页_交易数量().text
        self.assertAlmostEqual(float(total_money.split(' ')[0]), float(交易总额), delta=0.0001)
        self.assertAlmostEqual(float(total_money.split(' ')[0]), float(price.split(' ')[0])*float(数量), delta=0.0001)
        page.下单页_交易密码().send_keys('123456')
        self.assertEqual(account_data.密码密文*6, page.下单页_交易密码().text, '输入交易密码后显示不正确')

        page.选择页签('按数量').click()
        self.assertAlmostEqual(float(广告详情['数量'].split(' ')[0]),
                               float(page.下单页_数量或交易额编辑框().text.split('：')[1]), delta=0.0001)
        数量 = '1.2345'
        page.下单页_数量或交易额编辑框().send_keys(数量)
        total_money = page.下单页_交易总额().text
        # 数量 = page.下单页_最小限额().text
        self.assertEqual(广告详情['最小限额'], page.下单页_最小限额().text, '')
        self.assertEqual(广告详情['最大限额'], page.下单页_最大限额().text, '')
        self.assertAlmostEqual(float(total_money.split(' ')[0]), float(price.split(' ')[0]) * float(数量), delta=0.01)

    def test_002_验证法币页_购买出售功能(self):
        page = self.page
        page.选择法币币种页签('我要买').click()
        self.driver.implicitly_wait(5)
        币种 = 'USDT'
        page.选择法币币种页签(币种).click()
        self.driver.implicitly_wait(5)
        res = func.获取法币页广告数据(self.driver)
        广告详情 = res[1] if len(res) > 1 else res[0]
        #  法币下单
        下单数据 = {'下单方式': '按交易额', '价格或数量': 广告详情['最小限额'], '交易密码': '123456'}
        订单时间 = func.法币下单(self.driver, 下单数据)     # 2019-07-16T17:41:48

        # 获取订单详情
        # {'交易总额': '100.00CNY', '交易单价': '44.00CNY', '交易数量': '2.272727USDT', '订单号': '2156327011067082'}
        订单详情 = func.获取订单详情数据(self.driver)
        订单资源 = self.driver.page_source
        self.driver.back()
        self.driver.implicitly_wait(5)
        预期订单记录 = {'交易总额': re.findall(r"\d+.\d+", 订单详情['交易总额'])[0],
                  '交易数量': re.findall(r"\d+.\d+", 订单详情['交易数量'])[0],
                  '订单时间': strftime("%H:%M %m/%d", strptime(订单时间, "%Y-%m-%dT%H:%M:%S")),
                  '交易对象': 广告详情['名称'], '订单状态': '请付款', '币种': 币种}
        # [{'交易总额': '100.00', '交易数量': '2.272727', '订单时间': '17:41 07/16', '交易对象': '我是大魔王',
        # '订单状态': '请付款', '币种': 'USDT'}]
        func.法币页选择更多功能(self.driver, '订单记录')
        实际订单记录 = func.获取订单记录中数据(self.driver)
        self.assertIn(预期订单记录, 实际订单记录, '预期订单不在订单记录中')
        page.订单记录_订单状态()[0].click()
        self.driver.implicitly_wait(5)
        订单资源_new = self.driver.page_source
        self.assertEqual(订单资源, 订单资源_new, '订单详情应一致')

    def test_002_验证法币页发布广告功能_发布买单(self):
        # info = func.法币发布广告(self.driver, '1000', '2.5')
        info = {'币种': 'ETH', '法币': 'CNY', '总金额': '2500', '最大限额': '2500', '最小限额': '100', '单价': '1000', '数量': '2.5'}
        print(info)
        func.打开法币页管理公告(self.driver)
        info_list = func.获取管理广告中数据(self.driver)
        self.page.返回().click()
        sleep(1)
        print(info_list)
        昵称 = func.获取法币页昵称(self.driver)
        self.page.选择页签('我要卖').click()
        self.driver.implicitly_wait(5)
        self.page.选择页签(info['币种']).click()
        self.driver.implicitly_wait(5)
        if 昵称 in self.driver.page_source:
            订单数据 = func.获取法币页广告数据(self.driver)
        print(订单数据)
        self.assertEqual(info['单价'], info_list['单价'])
        self.assertEqual(info['数量'], info_list['数量'])
        self.assertEqual(info['币种'], info_list['币种'])
        self.assertEqual(info['法币'], info_list['法币'])
        self.assertEqual(info['最小限额']+' - '+info['最大限额'], info_list['限额'])

        预期广告数据 = {'单价': '1000.00 CNY', '数量': '2.500000 ETH', '名称': 'nikx0672', '最小限额': '100', '最大限额': '2500 CNY'}
        # 验证

    def test_003_验证法币页发布广告功能_发布卖单(self):
        info = func.法币发布广告(self.driver, '12345', '3.23', '300', '我要出售')
        print(info)
        func.打开法币页管理公告(self.driver)
        info_list = func.获取管理广告中数据(self.driver)
        self.page.返回().click()
        sleep(1)
        print(info_list)
        昵称 = func.获取法币页昵称(self.driver)
        self.page.选择页签('我要买').click()
        self.driver.implicitly_wait(5)
        self.page.选择页签(info['币种']).click()
        self.driver.implicitly_wait(5)
        if 昵称 in self.driver.page_source:
            订单数据 = func.获取法币页广告数据(self.driver)
        print(订单数据)
        self.assertEqual(info['单价'], info_list['单价'])
        self.assertEqual(info['数量'], info_list['数量'])
        self.assertEqual(info['币种'], info_list['币种'])
        self.assertEqual(info['法币'], info_list['法币'])
        self.assertEqual(info['最小限额'] + ' - ' + info['最大限额'], info_list['限额'])

    def test_004_验证法币页管理广告功能正常(self):
        page = self.page
        func.打开法币页管理公告(self.driver, '全部')
        info = func.获取管理广告中数据(self.driver)
        print(info)
        page.管理广告_查看成交明细()[0].click()
        self.driver.implicitly_wait(5)

    def test_005_验证法币页更多功能_法币设置(self):
        page = self.page
        法币对应单位 = {'美元': 'USD', '韩元': 'KRW', '日元': 'JPY', '欧元': 'EUR', '越南盾': 'VND', '人民币': 'CNY'}
        币种 = ['USDT', 'USDD', 'BTC', 'ETH']
        for key, value in 法币对应单位.items():
            func.法币页选择更多功能(self.driver, '法币设置')
            page.选择页签(key).click()
            page.返回().click()
            self.driver.implicitly_wait(5)
            for i in ['我要买', '我要卖']:
                page.选择页签(i).click()
                self.driver.implicitly_wait(5)
                for 币 in 币种:
                    page.选择页签(币).click()
                    self.driver.implicitly_wait(5)
                    elements = page.法币页广告_最大限额()
                    if len(elements) > 0:
                        te = page.法币页广告_最大限额()[0].text
                        print(te)
                        self.assertEqual(te.split(' ')[-1], value, '修改法币设置后不生效')
            page.法币页_增加广告().click()
            self.driver.implicitly_wait(5)
            page.法币页广告_发布广告按钮().click()
            self.driver.implicitly_wait(5)
            self.assertEqual(value, page.发布广告_使用法币().text, '发布广告页法币设置正确')
            page.返回().click()
            self.driver.implicitly_wait(5)

    def test_006_验证法币页更多功能_资金划转_页面显示(self):
        page = self.page
        func.法币页选择更多功能(self.driver, '资金划转')
        page.划转页面_币种().click()
        self.driver.implicitly_wait(5)
        page.选择页签('USDT').click()
        sleep(1)
        from账号 = page.划转页面_from账户().text
        to账号 = page.划转页面_to账户().text
        page.划转页面_账户交换().click()
        sleep(1)
        self.assertEqual(from账号, page.划转页面_to账户().text, '交换功能不正确')
        self.assertEqual(to账号, page.划转页面_from账户().text, '交换功能不正确')
        page.划转页面_账户交换().click()
        sleep(1)
        page.划转页面_全部按钮().click()
        账户可用数量 = page.划转页面_账户可用().text.split(' ')[1]
        self.assertEqual(page.划转页面_划转数量编辑框().text, 账户可用数量, '全部功能不正确')
        page.划转页面_划转数量编辑框().send_keys(str(float(账户可用数量)+10))
        self.assertEqual(page.划转页面_划转数量编辑框().text, 账户可用数量, '输入超过账户可用数量时，实际应是全部的数量')

    def test_007_验证法币页更多功能_资金划转(self):
        func.法币页选择更多功能(self.driver, '资金划转')
        币种 = 'USDT'
        划转金额 = '10.123'
        func.划转页面选择币种(self.driver, 币种)
        for from_account in ['币币账户', '法币账户']:
            划转前数量 = func.获取划转页面账户数量(self.driver)
            func.划转提现(self.driver, 划转金额, from_account)
            划转后数量 = func.获取划转页面账户数量(self.driver)
            func.验证划转提现功能正确(self, 划转前数量, 划转后数量, 划转金额, from_account)
        self.driver.back()

    def test_007_验证法币页更多功能_订单记录(self):
        func.法币页选择更多功能(self.driver, '订单记录')
        for 页签 in ['进行中', '已完成', '已取消', '全部']:
            订单记录 = func.获取订单记录中数据(self.driver, 页签)
            if 订单记录:
                print(订单记录[0])
                self.page.订单记录_订单时间()[0].click()
                sleep(2)
                if 页签 not in self.driver.page_source:
                    sleep(4)
                订单详情 = func.获取订单详情数据(self.driver, 订单记录[0]['订单状态'])
                print(订单详情)
                func.验证订单记录和订单详情中数据一致(self, 订单记录[0], 订单详情)
                self.driver.back()
                self.driver.implicitly_wait(5)

    def test_008_验证法币页更多功能_收款方式(self):
        func.法币页选择更多功能(self.driver, '收款方式')
        for e in self.page.收款方式_收款类型():
            print(e.text)
        self.page.收款方式_添加按钮().click()
        self.driver.implicitly_wait(3)

    def test_009_验证法币页更多功能_资金密码(self):
        func.法币页选择更多功能(self.driver, '资金密码')

    def test_010_验证法币页更多功能_我的昵称_修改成功(self):
        page = self.page
        func.法币页选择更多功能(self.driver, '我的昵称')
        name = func.随机生成名称()
        page.我的昵称_昵称编辑框().send_keys(name)
        page.我的昵称_保存按钮().click()
        sleep(1)
        页面资源 = self.driver.page_source
        self.assertIn('我要买', 页面资源, '昵称修改成功后应跳转到法币页面')
        self.assertIn('成功', 页面资源, '昵称修改成功后应跳转到法币页面')
        func.法币页选择更多功能(self.driver, '我的昵称')
        self.assertEqual(name, page.我的昵称_昵称编辑框().text, '再次点击昵称后显示名称不正确')
        page.返回().click()

    def test_011_验证法币页更多功能_我的昵称_修改失败(self):
        page = self.page
        func.法币页选择更多功能(self.driver, '我的昵称')
        page.我的昵称_保存按钮().click()
        sleep(1)
        页面资源 = self.driver.page_source
        self.assertIn('我的昵称', 页面资源, '昵称修改成功后应跳转到法币页面')
        self.assertIn('昵称重复', 页面资源, '昵称修改成功后应跳转到法币页面')
