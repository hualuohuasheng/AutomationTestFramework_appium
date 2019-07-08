# -*- coding:utf-8 -*-

from xinyuan.app.appelement.user import UserPage
from xinyuan.app.appelement.币币页 import 币币页
from unittest import TestCase
from time import sleep


def log_out(driver):
    user_page = UserPage(driver)
    user_page.进入用户页面按钮().click()
    sleep(1)
    if '请登录' not in user_page.用户名().text:
        user_page.设置().click()
        sleep(0.5)
        user_page.设置_退出().click()
        sleep(0.5)
    user_page.用户名().click()
    sleep(1)


def log_in(driver, account, password, googlecode=None):
    page = UserPage(driver)
    page.账号编辑框().send_keys(account)
    page.密码编辑框().send_keys(password)
    page.登录按钮().click()

    if googlecode is not None:
        page.安全验证_谷歌认证_谷歌验证码().send_keys(googlecode)


def forget_password(driver, account, bindingphone=True, bindingemail=False, bindinggoogle=False):
    page = UserPage(driver)
    page.忘记密码按钮().click()
    sleep(0.5)
    page.忘记密码_账号编辑框().send_keys(account)
    page.下一步().click()
    sleep(0.5)
    if bindingphone:
        # page.安全验证_发送手机验证码().click()
        page.安全验证_输入手机验证码().send_keys('123456')
    if bindingemail:
        # page.安全验证_发送邮箱验证码().click()
        page.安全验证_输入邮箱验证码().send_keys('123456')
    if bindinggoogle:
        page.安全验证_谷歌认证_输入谷歌验证码().send_keys('123456')

    page.下一步().click()
    sleep(0.5)
    page.安全验证_提交().click()


def switch_to_register(driver, way='email'):
    # 注册方式为2中，分为邮箱注册和手机注册
    page = UserPage(driver)
    page.免费注册按钮().click()
    sleep(10)

    if way=='phone':
        size = driver.get_window_size()
        print(size)
        driver.swipe(size['width'] - 20, size['height'] / 2, size['width'] - 20, size['height'] / 5, duration=500)
        page.手机注册().click()
        sleep(0.2)


def register_by_phone(driver, phone, username, pwd, repwd):
    page = UserPage(driver)
    switch_to_register(driver, 'phone')
    size = driver.get_window_size()
    # page.国家().click()
    # sleep(1)
    # page.选择国家('Vietnam').click()
    # sleep(0.5)
    page.账号编辑框().send_keys(phone)
    page.昵称编辑框().send_keys(username)
    # self.page.安全验证_发送手机验证码().click
    page.安全验证_输入手机验证码().send_keys()
    page.密码编辑框().send_keys(pwd)
    sleep(1)
    page.密码确认编辑框().send_keys(repwd)
    sleep(1)
    page.同意条款按钮().click()
    driver.swipe(size['width'] - 20, size['height'] / 2, size['width'] - 20, size['height'] / 5, duration=500)
    page.注册按钮().click()


def register_by_email(driver, email, username, pwd):
    page = UserPage(driver)
    switch_to_register(driver, 'email')
    page.账号编辑框().send_keys(email)
    page.昵称编辑框().send_keys(username)
    page.密码编辑框().send_keys(pwd)
    sleep(1)
    page.同意条款按钮().click()
    page.注册按钮().click()
    sleep(15)
    page.电子邮件已经验证按钮().click()
    sleep(3)


def modify_login_password(driver, old_pwd, new_pwd):
    page = UserPage(driver)
    page.安全验证().click()
    sleep(2)
    page.安全验证_登录密码().click()
    sleep(1)
    page.安全验证_登录密码_输入密码().send_keys(old_pwd)
    page.下一步().click()
    sleep(1)
    page.安全验证_登录密码_新密码().send_keys(new_pwd)
    page.安全验证_登录密码_确认新密码().send_keys(new_pwd)
    page.安全验证_提交().click()
    sleep(10)


def 验证是否登录(driver, account, pwd):
    user_page = UserPage(driver)
    user_page.进入用户页面按钮().click()
    sleep(2)
    user_name = user_page.用户名().text
    if '请登录' in user_name:
        user_page.用户名().click()
        sleep(10)
        log_in(driver, account, pwd)
        sleep(15)
    driver.back()


def 选择币种(driver, coins):
    page = 币币页(driver)
    if coins.lower() == page.币种标题显示().text.lower():
        return
    page.币种标题显示().click()
    sleep(1)
    page.搜索按钮().click()
    driver.implicitly_wait(5)
    page.搜索输入框().send_keys(coins)
    page.搜索_结果().click()
    sleep(1)


def 下单(driver, price, amount, orderway='买入'):
    page = 币币页(driver)
    if orderway == '买入':
        page.买入标签按钮().click()
    else:
        page.卖出标签按钮().click()
    driver.implicitly_wait(2)
    old_amount = page.币种可用数量显示().text
    page.获取盘口所有价格()[4].click()
    page.价格编辑框().send_keys(price)
    page.数量编辑框().send_keys(amount)
    driver.tap([[200, 10]])
    page.买入按钮().click()
    sleep(2)
    return old_amount


def 验证下单后当前委托显示正确(driver, expected_res):
    page = 币币页(driver)
    size = driver.get_window_size()
    driver.swipe(size['width'] - 100, size['height'] * 4 / 5, size['width'] - 100, size['height'] / 5, duration=500)
    print(expected_res)
    # elements = page.获取当前委托所有订单币种()
    for e in page.获取当前委托所有订单币种():
        '1'.upper()
        TestCase.assertEqual(e.text, expected_res['币种'].upper(), '币种显示正确')
    for e in page.获取当前委托所有订单数量():
        TestCase.assertEqual(e.text, expected_res['数量'], '币种显示正确')
        print(e.text)
    for e in page.获取当前委托所有订单价格():
        TestCase.assertEqual(e.text, expected_res['价格'], '币种显示正确')
        print(e.text)
    for e in page.获取当前委托所有订单时间():
        # TestCase.assertEqual(e.text, expected_res['时间'], '币种显示正确')
        print(e.text)
