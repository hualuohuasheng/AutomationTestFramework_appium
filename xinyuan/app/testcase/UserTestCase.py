# -*- coding:utf-8 -*-

import unittest
from xinyuan.app.appelement.user import UserPage
import xinyuan.app.testcase.device as device
import xinyuan.app.testcase.user_functions as func
from appium import webdriver
from time import sleep
import xinyuan.app.data.account_data as account_data


class UserLogInTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.desired_caps = device.Device.caps
        cls.driver = webdriver.Remote(f"http://localhost:4723/wd/hub", cls.desired_caps)
        sleep(10)

    def setUp(self):
        self.page = UserPage(self.driver)
        func.log_out(self.driver)

    def tearDown(self):
        pass
        # self.driver.back()

    def test_001_验证登录正确(self):
        func.log_in(self.driver, account_data.普通全新账号['account'], account_data.普通全新账号['pwd'])
        sleep(15)
        user_name = self.page.用户名().text
        self.assertNotEqual('请登录', user_name, '登录失败')

    def test_002_验证登录页面隐藏显示密码正确(self):
        self.page.账号编辑框().send_keys(account_data.普通全新账号['account'])
        self.page.密码编辑框().send_keys(account_data.普通全新账号['pwd'])

        self.page.隐藏显示密码().click()
        sleep(0.5)
        self.assertEqual(account_data.普通全新账号['pwd'], self.page.密码编辑框().text, '显示密码错误')

        self.page.隐藏显示密码().click()
        sleep(0.5)
        self.assertEqual('••••••••••••••', self.page.密码编辑框().text, '隐藏密码显示错误')
        self.driver.back()

    def test_003_验证登录时账号密码为必选项(self):
        self.page.账号清除按钮().click()
        self.page.登录按钮().click()
        self.assertIn('请输入账号', self.driver.page_source, '应提示输入账号')
        self.page.账号编辑框().send_keys(account_data.普通全新账号['account'])
        self.page.登录按钮().click()
        self.assertIn('请输入密码', self.driver.page_source, '应提示输入账号')
        self.driver.back()

    def test_004_验证登录功能时账号密码输入错误提示信息正确(self):
        func.log_in(self.driver, account_data.普通全新账号['account'], '123456sdf')
        self.assertIn('登录账号或密码不正确', self.driver.page_source, '应提示登录账号或密码不正确')
        func.log_in(self.driver, '1' + account_data.普通全新账号['account'], account_data.普通全新账号['pwd'])
        self.assertIn('登录账号或密码不正确', self.driver.page_source, '应提示登录账号或密码不正确')

    def test_005验证带有谷歌验证码的账号登录正确(self):
        func.log_in(self.driver, account_data.有谷歌验证码的账号['account'], account_data.有谷歌验证码的账号['pwd'],
                    '123456')
        user_name = self.page.用户名().text
        self.assertNotEqual('请登录', user_name, '登录失败')

    def test_006_验证登录_谷歌验证码输入不正确时提示信息正确(self):
        func.log_in(self.driver, account_data.有谷歌验证码的账号['account'], account_data.有谷歌验证码的账号['pwd'],
                    '123123')
        self.assertIn('请输入密码', self.driver.page_source, '应提示输入账号')
        self.driver.back()

    def test_007_验证忘记密码功能正确(self):
        func.forget_password(self.driver, account_data.手机账号['account'])
        func.forget_password(self.driver, account_data.邮箱账号['account'], False, True)
        func.forget_password(self.driver, account_data.kyc账号['account'], True, True, True)

    def test_008_验证手机注册成功(self):
        func.register_by_phone(self.driver, '15811055254', 'test123123', 'test1234', 'test1234')
        func.log_in(self.driver, '15811055254', 'test1234')
        user_name = self.page.用户名().text
        self.assertNotEqual('请登录', user_name, '登录失败')

    def test_009_验证邮箱注册成功(self):
        func.register_by_email(self.driver, 'mingleili@xinmoney.cn', 'test0002', 'test1234')
        func.log_in(self.driver, 'mingleili@xinmoney.cn', 'test1234')
        user_name = self.page.用户名().text
        self.assertNotEqual('请登录', user_name, '登录失败')


class UserManageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.desired_caps = device.Device.caps
        cls.driver = webdriver.Remote(f"http://localhost:4723/wd/hub", cls.desired_caps)
        sleep(10)

    def setUp(self):
        self.page = UserPage(self.driver)
        self.page.进入用户页面按钮().click()
        sleep(2)
        user_name = self.page.用户名().text
        if '请登录' in user_name:
            self.page.用户名().click()
            sleep(10)
            func.log_in(self.driver, account_data.普通全新账号['account'], account_data.普通全新账号['pwd'])
            sleep(15)

    def tearDown(self):
        pass

    def test_001_安全验证_修改登录密码成功(self):
        old_pwd = account_data.普通全新账号['pwd']
        new_pwd = 'test1234'
        func.modify_login_password(self.driver, old_pwd, new_pwd)
        func.log_in(self.driver, account_data.普通全新账号['account'], new_pwd)
        sleep(20)
        user_name = self.page.用户名().text
        self.assertNotEqual('请登录', user_name, '修改密码后登录失败')
        func.modify_login_password(self.driver, new_pwd, old_pwd)
        func.log_in(self.driver, account_data.普通全新账号['account'], old_pwd)
        sleep(20)

    def test_002_安全验证_设置交易密码(self):
        self.page.安全验证().click()
        self.driver.implicitly_wait(5)
        self.page.安全验证_修改交易密码().click()
        sleep(1)
        self.page.安全验证_登录密码_输入密码().send_keys(account_data.有谷歌验证码的账号['pwd'])
        self.page.安全验证_输入手机验证码().send_keys('123456')
        self.page.安全验证_输入邮箱验证码().send_keys('123456')
        self.page.下一步().click()
        # self.page.交易

    def test_003_安全验证_修改交易密码时效(self):
        self.page.安全验证().clicl()
        self.driver.implicitly_wait(5)
        self.page.安全验证_交易密码时效().click()
        self.driver.implicitly_wait(5)
