# -*- coding:utf-8 -*-

from xinyuan.app.appelement.user import UserPage
from xinyuan.app.appelement.行情页 import 行情页
from xinyuan.app.appelement.币币页 import 币币页
from xinyuan.app.appelement.法币页 import 法币页
from xinyuan.app.appelement.资产页 import 资产页
from time import sleep
import time
import datetime
import xml.etree.ElementTree as ET
import re
import random


"""" 执行操作的相关函数 """


def 格式化浮点数(num, 位数=2):
    1


def 随机生成名称():
    rand_str = ''.join(random.sample('zxcvbnmasdfghjklqwertyuiop', 4))
    rand_int = ''.join(random.sample('1234567890', 4))
    return rand_str + rand_int


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
        driver.swipe(start_x, start_y, end_x, end_y, duration=None)
    else:
        driver.execute_script()


def 向下滑动(driver, side='右侧', duration=500):
    size = driver.get_window_size()
    if side == '右侧':
        滑动页面(driver, size['width'] - 100, size['height'] * 3 / 5, size['width'] - 100, size['height'] * 2 / 5, duration)
    else:
        滑动页面(driver, 100, size['height'] * 4 / 5, 100, size['height'] / 5, duration)


def 向上滑动(driver, side='右侧', duration=500):
    size = driver.get_window_size()
    if side == '右侧':
        滑动页面(driver, size['width'] - 100, size['height'] / 5, size['width'] - 100, size['height'] * 4 / 5, duration)
    else:
        滑动页面(driver, 100, size['height'] / 5, 100, size['height'] * 4 / 5, duration)


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


def 法币发布广告(driver, 价格, 数量, 最小限额='default', way='我要购买'):
    page = 法币页(driver)
    page.法币页_增加广告().click()
    driver.implicitly_wait(5)
    page.法币页广告_发布广告按钮().click()
    driver.implicitly_wait(3)
    page.选择页签(way).click()
    driver.implicitly_wait(2)
    res = {'币种': page.发布广告_买卖币种().text, '法币': page.发布广告_使用法币().text, '单价': 价格, '数量': 数量}
    if way == '我要购买':
        page.发布广告_购买价格().send_keys(价格)
        page.发布广告_购买数量().send_keys(数量)
        res['总金额'] = page.发布广告_购买总金额().text
    else:
        page.发布广告_出售价格().send_keys(价格)
        page.发布广告_出售数量().send_keys(数量)
        page.发布广告_出售总金额()
        res['总金额'] = page.发布广告_出售总金额().text
    page.发布广告_交易方式().click()
    sleep(2)
    size = driver.get_window_size()
    driver.tap([[size['width'] / 2, size['height'] - 100]])
    sleep(1)
    driver.tap([[size['width'] / 2, 100]])
    sleep(2)
    if 最小限额 == 'default':
        最小限额 = page.发布广告_最小限额().text
    page.发布广告_最小限额().send_keys(最小限额)
    res['最大限额'] = page.发布广告_最大限额().text
    res['最小限额'] = page.发布广告_最小限额().text
    向下滑动(driver, '左侧')
    page.发布广告_发布广告按钮().click()
    sleep(0.5)
    if '撤单或支付超时次数已达最大限制' in driver.page_source:
        res = {}
        driver.back()
    return res


def 打开法币页管理公告(driver, 页签='进行中'):
    page = 法币页(driver)
    page.法币页_增加广告().click()
    driver.implicitly_wait(5)
    page.法币页广告_管理广告按钮().click()
    driver.implicitly_wait(5)
    page.选择页签(页签).click()
    sleep(0.5)


# 下单数据 = {'下单方式': '按交易额', '价格或数量': '123', '交易密码: '123456'}
def 法币下单(driver, 下单数据):
    page = 法币页(driver)
    page.法币页广告_购买出售按钮()[1].click()
    driver.implicitly_wait(5)
    page.选择页签(下单数据['下单方式']).click()
    page.下单页_数量或交易额编辑框().send_keys(下单数据['价格或数量'])
    page.下单页_交易密码().send_keys(下单数据['交易密码'])
    page.下单页_立即下单按钮().click()
    local_time = get_local_time()
    sleep(1)
    return local_time


def 法币页选择更多功能(driver, 功能名称):
    page = 法币页(driver)
    page.法币页更多设置().click()
    driver.implicitly_wait(5)
    page.选择页签(功能名称).click()
    driver.implicitly_wait(5)


def 划转页面选择币种(driver, 币种):
    page = 法币页(driver)
    if page.划转页面_币种().text != 币种:
        page.划转页面_币种().click()
        driver.implicitly_wait(5)
        page.选择页签(币种).click()
        sleep(1)


def 划转提现(driver, 划转数量, from_account='币币账户'):
    page = 法币页(driver)
    if from_account != page.划转页面_from账户().text:
        page.划转页面_账户交换().click()
        sleep(1)
    page.划转页面_划转数量编辑框().send_keys(划转数量)
    page.划转页面_划转按钮().click()
    driver.implicitly_wait(10)


def 资产页搜索币种(driver, 币种名称):
    page = 资产页(driver)
    page.资产页_币种资产_搜索按钮().click()
    sleep(0.5)
    page.资产页_币种资产_搜索编辑框().send_keys(币种名称)


def 执行提现(driver, 提现数据):
    page = 资产页(driver)
    page.资产页_资产细节_提现按钮().click()
    driver.implicitly_wait(5)
    driver.back()
    page.提现页面_提现数量编辑框().send_keys(提现数据['提现数量'])
    page.提现页面_提现地址编辑框().send_keys(提现数据['提现地址'])
    print(page.提现页面_手续费().text)
    page.button('下一步').click()
    driver.implicitly_wait(4)
    page.提现页面_提现数量编辑框()


"""" 获取数据的相关函数 """


def 获取行情页编辑自选通证页的数据(driver):
    page = 行情页(driver)
    res = []
    for i in range(len(page.编辑通证_交易对币种())):
        币种 = page.编辑通证_交易对币种()[i].text
        计价方式 = page.编辑通证_交易对计价币种()[i].text
        print(币种, 计价方式)
        res.append(币种 + 计价方式)
    return res


def 获取行情页币种交易对数据(driver):
    page = 行情页(driver)
    res = []
    for i in range(len(page.币种列表_币种名称())):
        info = {"币种": page.币种列表_币种名称()[i].text, "计价名称": page.币种列表_币种计价方式名称()[i].text,
                "24H量": page.币种列表_24H量()[i].text, "最新价": page.币种列表_最新价格按钮()[i].text,
                "最新价换算价格": page.币种列表_换算为当前资产计价方式按钮()[i].text, '涨跌幅': page.币种列表_涨跌幅按钮()[i].text}
        res.append(info)
    print(res)
    return res


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


def 获取法币页广告数据(driver):
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


def 获取法币页昵称(driver):
    page = 法币页(driver)
    法币页选择更多功能(driver, '我的昵称')
    昵称 = page.我的昵称_昵称编辑框().text
    page.返回().click()
    sleep(0.5)
    return 昵称


def 获取划转页面账户数量(driver):
    page = 法币页(driver)
    res = {page.划转页面_from账户().text : page.划转页面_账户可用().text}
    page.划转页面_账户交换().click()
    sleep(2)
    res[page.划转页面_from账户().text] = page.划转页面_账户可用().text
    return res


def 获取订单记录中数据(driver, 页签='进行中'):
    page = 法币页(driver)
    page.选择页签(页签).click()
    driver.implicitly_wait(5)
    订单记录结果 = []
    订单交易对象 = page.订单记录_交易对象名称()
    if 订单交易对象:
        for i in range(len(订单交易对象)):
            订单记录 = dict(交易总额=page.订单记录_交易金额()[i].text, 交易数量=page.订单记录_订单数量()[i].text,
                        订单时间=page.订单记录_订单时间()[i].text, 交易对象=page.订单记录_交易对象名称()[i].text,
                        订单状态=page.订单记录_订单状态()[i].text, 币种=page.订单记录_币种()[i].text)
            订单记录结果.append(订单记录)
    return 订单记录结果


def 获取订单详情数据(driver, 订单详情状态='请付款'):
    page = 法币页(driver)
    订单详情状态 = '等待放行' if '放币超时' in 订单详情状态 else 订单详情状态
    if '请付款' in 订单详情状态:
        订单详情 = dict(交易总额=page.订单记录_进行中订单详情_交易总额().text, 交易单价=page.订单记录_进行中订单详情_交易单价().text,
                    交易数量=page.订单记录_进行中订单详情_交易数量().text, 订单号=page.订单记录_进行中订单详情_订单号().text,
                    订单状态=page.订单记录_订单详情_订单状态().text)
    elif '等待放行' in 订单详情状态:
        订单详情 = dict(交易总额=page.订单记录_放币超时_订单详情_交易总额().text, 交易单价=page.订单记录_放币超时_订单详情_交易单价().text,
                    交易数量=page.订单记录_放币超时_订单详情_交易数量().text, 订单号=page.订单记录_放币超时_订单详情_订单号().text,
                    订单状态=page.订单记录_订单详情_订单状态().text)
    else:
        订单详情 = dict(交易总额=page.订单记录_取消订单详情_交易总额().text, 交易单价=page.订单记录_取消订单详情_交易单价().text,
                    交易数量=page.订单记录_取消订单详情_交易数量().text, 订单号=page.订单记录_取消订单详情_订单号().text,
                    交易对象=page.订单记录_取消订单详情_收款人().text, 订单时间=page.订单记录_取消订单详情_下单时间().text,
                    订单状态=page.订单记录_订单详情_订单状态().text)
    return 订单详情


def 获取管理广告中数据(driver):
    page = 法币页(driver)
    info = {
        '单价': page.管理广告_单价()[0].text,
        '币种': page.管理广告_广告币种()[0].text,
        '数量': page.管理广告_数量()[0].text,
        '已成交量': page.管理广告_已成交量()[0].text,
        '订单时间': page.管理广告_订单时间()[0].text,
        '限额': page.管理广告_限额()[0].text,
        '广告状态': page.管理广告_广告状态()[0].text,
        '法币': page.管理广告_交易货币()[0].text
    }
    return info


def 获取资产页资产统计数据(driver):
    page = 资产页(driver)
    res = dict(合计=page.资产页_资产汇总_资产合计显示().text, 标题=page.资产页_资产汇总_标题按钮().text,
               换算=page.资产页_资产汇总_换算金额显示().text)
    return res


def 获取资产页各币种资产数据(driver):
    page = 资产页(driver)
    币种名称 = page.资产页_币种资产_币种名称()
    res = []
    for i in range(len(币种名称)):
        res_tmp = dict(币种名称=page.资产页_币种资产_币种名称()[i].text, 币种详细名称=page.资产页_币种资产_币种详细名称()[i].text,
                       数量=page.资产页_币种资产_币种数量()[i].text, 换算数量=page.资产页_币种资产_币种换算金额()[i].text)
        res.append(res_tmp)
    print(res)
    return res


"""" 验证功能的相关函数 """


def 验证是否登录(driver, account, pwd):
    user_page = UserPage(driver)
    user_page.进入用户页面按钮().click()
    sleep(2)
    user_name = user_page.用户名().text
    print(user_page.uid().text)
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


def 验证划转提现功能正确(obc, 划转前数量, 划转后数量, 划转金额, from_account='币币账户'):
    预期 = float(划转前数量[from_account].split(' ')[1]) - float(划转金额)
    实际 = float(划转后数量[from_account].split(' ')[1])
    obc.assertAlmostEqual(预期, 实际, delta=0.001)
    to_account = '法币账户' if from_account == '币币账户' else '币币账户'
    print(from_account, to_account)
    预期增加 = float(划转前数量[to_account].split(' ')[1]) + float(划转金额)
    实际数据 = float(划转后数量[to_account].split(' ')[1])
    obc.assertAlmostEqual(预期增加, 实际数据, delta=0.001)


def 验证订单记录和订单详情中数据一致(obc, 订单记录数据, 订单详情数据):
    if '交易对象' in 订单详情数据.keys():
        obc.assertEqual(订单记录数据['交易对象'], 订单详情数据['交易对象'], '订单详情中的交易对象和订单记录中不一致')
        订单详情时间 = time.strftime("%H:%M %m/%d", time.strptime(订单详情数据['订单时间'], "%Y-%m-%d %H:%M:%S"))
        obc.assertEqual(订单记录数据['订单时间'], 订单详情时间, '订单详情中的交易对象和订单记录中不一致')
    预期订单详情状态 = '等待放行' if 订单记录数据['订单状态'] == '放币超时' else 订单记录数据['订单状态']
    obc.assertIn(预期订单详情状态, 订单详情数据['订单状态'], '订单状态显示正确')
    obc.assertEqual(订单记录数据['交易总额'], 订单详情数据['交易总额'][0:-3], '订单详情中的交易对象和订单记录中不一致')
    obc.assertEqual(订单记录数据['交易数量']+订单记录数据['币种'], 订单详情数据['交易数量'], '订单详情中的交易对象和订单记录中不一致')
