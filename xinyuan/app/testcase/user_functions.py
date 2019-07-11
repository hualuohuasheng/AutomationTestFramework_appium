# -*- coding:utf-8 -*-

from xinyuan.app.appelement.user import UserPage
from xinyuan.app.appelement.币币页 import 币币页
from xinyuan.app.appelement.法币页 import 法币页
from time import sleep
import time
import datetime
import xml.etree.ElementTree as ET
import re


"""" 执行操作的相关函数 """


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


def get_local_time():
    res = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
    return res


def 滑动页面(driver, start_x, start_y, end_x, end_y, duration):
    if UserPage(driver).is_android:
        driver.swipe(start_x, start_y, end_x, end_y, duration=duration)
    else:
        driver.execute_script()


def 获取历史委托中日期时间(source):
    with open('tmp.xml', 'w') as f:
        f.write(source)
    tree = ET.ElementTree(file='tmp.xml')
    res_date, res_time = [], []
    for e in tree.iterfind(".//android.widget.TextView[@resource-id='com.ex55.app:id/tvOrderDateTime']"):
        res_date.append(e.attrib['text'])
    for e in tree.iterfind(".//android.widget.TextView[@resource-id='com.ex55.app:id/tvOrderTime']"):
        res_time.append(e.attrib['text'])
    print(res_time, res_date)
    print(reversed(res_time), reversed(res_date))
    if len(res_time) != len(res_date):
        res = [reversed(res_date)[i] + " " + reversed(res_time)[i] for i in range(min(len(res_time), len(res_date)))]
    else:
        res = [res_date[i] + " " + res_time[i] for i in range(len(res_time))]
    print(res)


def log_in(driver, account, password, googlecode=None):
    page = UserPage(driver)
    page.账号编辑框().send_keys(account)
    page.密码编辑框().send_keys(password)
    page.登录按钮().click()

    if googlecode is not None:
        page.安全验证_谷歌认证_输入谷歌验证码().send_keys(googlecode)


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

    if way == 'phone':
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


def 选择币种(driver, coins):
    page = 币币页(driver)
    if coins.lower() == re.sub(' ', '', page.币种标题显示().text.lower()):
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
    sleep(2)
    old_amount = page.币种可用数量显示().text
    page.获取盘口所有价格()[4].click()
    page.价格编辑框().send_keys(price)
    page.数量编辑框().send_keys(amount)
    driver.tap([[200, 10]])
    if orderway == '买入':
        page.买入按钮().click()
    else:
        page.卖出按钮().click()
    order_time = driver.device_time
    sleep(2)
    return old_amount, order_time


def 历史委托中筛选(driver, conditions):
    page = 币币页(driver)
    page.历史委托_筛选按钮().click()
    driver.implicitly_wait(5)
    for e in conditions:
        print(e[0], e[1])
        page.历史委托_筛选_table按钮(e[0])[e[1]].click()
        sleep(0.5)
    page.历史委托_筛选_确认按钮().click()

    if len(page.获取当前委托所有订单币种()) > 0:
        size = driver.get_window_size()
        while True:
            page_source_1 = driver.page_source
            滑动页面(driver, size['width'] - 100, size['height'] * 4 / 5, size['width'] - 100, size['height'] / 5, 200)
            page_source_2 = driver.page_source
            if page_source_1 == page_source_2:
                break


"""" 获取数据的相关函数 """


def 获取下单后当前委托数据(driver, isswip=True):
    page = 币币页(driver)
    if isswip:
        size = driver.get_window_size()
        sleep(3)
        滑动页面(driver, size['width'] - 100, size['height'] * 4 / 5, size['width'] - 100, size['height'] / 5, 500)
    real_res = []
    币种 = page.获取当前委托所有订单币种()
    print(len(币种))
    for i in range(len(币种)):
        res = {'币种': page.获取当前委托所有订单币种()[i].text,
               '属性': page.获取当前委托所有订单状态()[i].text,
               '数量': page.获取当前委托所有订单数量()[i].text,
               '价格': page.获取当前委托所有订单价格()[i].text,
               '时间': page.获取当前委托所有订单时间()[i].text,
               '日期': page.获取当前委托所有订单日期()[i].text
               }
        real_res.append(res)
    print(real_res)
    return real_res


def 获取盘口所有数据(elements):
    price_list = [float(e.text) for e in elements]
    while len(set(price_list)) == 1:
        sleep(1)
        print(f'this is {price_list}')
        获取盘口所有数据(elements)
    print(price_list)
    return price_list


def 获取下单后历史委托数据(driver):
    page = 币币页(driver)
    page.右上更多功能按钮().click()
    driver.implicitly_wait(5)
    page.历史委托按钮().click()
    driver.implicitly_wait(5)

    时间戳 = time.mktime(
        time.strptime(page.获取当前委托所有订单日期()[0].text + 'T' + page.获取当前委托所有订单时间()[0].text, "%Y-%m-%dT%H:%M:%S"))
    res = {'币种': page.获取当前委托所有订单币种()[0].text,
           '属性': page.获取当前委托所有订单状态()[0].text,
           '数量': page.获取当前委托所有订单数量()[0].text,
           '价格': float(page.获取当前委托所有订单价格()[0].text),
           '时间戳': 时间戳,
           '状态': page.获取当前委托所有订单取消()[0].text
           }
    driver.back()
    return res


def 获取买币页的广告数据(driver):
    page = 法币页(driver)
    res_单价 = [i.text for i in page.法币页广告_单价()]
    res_数量 = [i.text for i in page.法币页广告_数量()]
    res_名称 = [i.text for i in page.法币页广告_名称()]
    res_最小限额 = [i.text for i in page.法币页广告_最小限额()]
    res_最大限额 = [i.text for i in page.法币页广告_最大限额()]
    result = []
    for i in range(len(res_数量)):
        market_info = {'单价': res_单价[i], '数量': res_数量[i], '名称': res_名称[i], '最小限额': res_最小限额[i],
                       '最大限额': res_最大限额[i]}
        result.append(market_info)
    return result


"""" 验证功能的相关函数 """


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


def 验证下单前后数量显示是否正确(obc, amount_befor_order, amount_after_order, expected):
    if expected['属性'] == '买入':
        # 订单买入，可用数量按usdt数量显示, 成交后=买入前的数量-价格*数量
        obc.assertAlmostEqual(float(amount_befor_order) - float(expected['数量']) * expected['价格'],
                              float(amount_after_order), delta=0.1)
    else:
        # 订单卖出，可用数量按eth数量显示, 成交后=买入前的数量-数量
        obc.assertAlmostEqual(float(amount_befor_order) - float(expected['数量']), float(amount_after_order), delta=0.01)


def 验证委托数据和预期结果一致(obc, expected, history_order):
    for key in expected.keys():
        if '时间戳' in key:
            obc.assertAlmostEqual(expected[key], history_order[key], delta=5)
        else:
            obc.assertEqual(expected[key], history_order[key], f'{key}的值对比错误')


def 验证历史委托中按时间筛选正确(obc, actual_time, expected_days):
    cur_day = datetime.datetime.now()
    actual_day = datetime.datetime.strptime(actual_time, '%Y-%m-%d')
    obc.assertTrue((cur_day - actual_day).days <= expected_days, '时间筛选不正确')
