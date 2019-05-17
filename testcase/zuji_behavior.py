# -*- coding:utf-8 -*-

from time import sleep
import lib.public_functions as pubfuc
from appium.webdriver.common.touch_action import TouchAction
import logging

logger = logging.getLogger('autolog')

# ios 控件
# 开始比赛：


def backiosapp(driver, size, appid, time=5):
    x = size['width'] - 30
    y = size['height'] - 30
    driver.tap([[x, y]])  # iphone辅助功能按键放置在右下角
    sleep(2)
    x = size['width'] / 2
    y = size['height'] - 138
    driver.tap([[x, y]])
    sleep(time)
    driver.activate_app(appid)


def logout(driver):
    driver.find_element_by_xpath("//android.widget.TextView[@text='我的']").click()
    sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@text='设置']").click()
    sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@text='退出登录']").click()
    sleep(1)
    driver.find_element_by_xpath("//android.widget.Button[@text='确定']").click()


def loginbyphonenumber(driver):
    driver.find_element_by_xpath("//android.widget.EditText[@text='请输入手机号']").send_keys('18610122196')
    driver.find_element_by_xpath("//android.widget.EditText[@text='请输入密码']").send_keys('sjdd1234')
    driver.tap([[200, 200]])  # 点击空白处返回按钮
    sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@text='登录']").click()
    # s1 = driver.find_element_by_xpath("//android.widget.TextView[@text='微信']").size
    # s2 = driver.find_element_by_xpath("//android.widget.TextView[@text='微信']").location
    # driver.tap([[s2['x']+50, s2['y']-60]])
    # driver.find_element_by_xpath("//android.widget.ViewGroup/android.widget.ViewGroup").click()
    sleep(3)
    driver.find_element_by_xpath("//android.widget.TextView[@text='登录成功']")
    driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()


def login(driver, devicename):
    failcount = 3  # 用例中出错后重新执行的次数
    runcount = 1
    num = 1
    elementinfo, deviceid = pubfuc.getiteminfo(driver.desired_capabilities, 'zuji')
    while True:
        try:
            if runcount > failcount:
                break
            driver.find_element_by_xpath(elementinfo['我的']['xpath']).click()
            sleep(1)
            if '请登录' in driver.page_source:
                driver.find_element_by_xpath("//android.widget.TextView[@text='请登录']").click()
            else:
                logout(driver)
            while num < 501:
                logger.info(f'第{num}次登录')
                sleep(2)
                loginbyphonenumber(driver)
                sleep(2)
                driver.tap([[200, 200]])
                logout(driver)
                num += 1
            sleep(2)
            # 为保证接下来用例正常运行，测试完登录功能后登录账户
            loginbyphonenumber(driver)
            break
        except Exception as e:
            logger.info(f'第{num}次运行出错，设备是:{devicename}')
            err_time = pubfuc.getlocaltime()
            img_file = pubfuc.get_real_dir_path(__file__, f'../testresult/{err_time}-{devicename}.png')
            driver.save_screenshot(str(img_file))
            sleep(3)
            logger.error(e.args[0], exc_info=True)
            logger.info(f'第{runcount}次重跑')
            runcount += 1
            driver.close_app()
            driver.launch_app()
            logger.info(pubfuc.getlocaltime())
            sleep(20)


def create_game(driver, elementinfo):
    driver.find_element_by_xpath(elementinfo['加号']['xpath']).click()
    sleep(1)
    driver.find_element_by_xpath(elementinfo['创建比赛']['xpath']).click()
    sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@text='我的测试队']").click()
    sleep(0.5)
    driver.find_element_by_xpath("//android.widget.TextView[@text='下一步']").click()
    sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@text='下一步']").click()
    sleep(1)
    driver.find_element_by_xpath(elementinfo['拍摄']['xpath']).click()
    sleep(1)
    driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
    sleep(1)


def get_game_code(driver, elementinfo):
    driver.find_element_by_xpath(elementinfo['添加设备']['xpath']).click()
    sleep(1)
    driver.find_element_by_xpath(elementinfo['比赛口令码']['xpath']).click()
    sleep(1)
    password = driver.find_element_by_xpath(elementinfo['口令码']['xpath']).text
    sleep(1)
    driver.tap([[300, 300]])
    print(password)
    sleep(1)
    return password


def join_game_by_code(driver, elementinfo, code):
    driver.find_element_by_xpath(elementinfo['加号']['xpath']).click()
    sleep(1)
    driver.find_element_by_xpath(elementinfo['加入比赛']['xpath']).click()
    sleep(1)
    driver.find_element_by_xpath(elementinfo['口令']['xpath']).click()
    sleep(1)
    driver.find_element_by_xpath(elementinfo['输入口令']['xpath']).send_keys(code)
    driver.press_keycode(66)
    driver.find_element_by_xpath(elementinfo['口令确定']['xpath']).click()
    sleep(1)
    driver.find_element_by_xpath(elementinfo['拍摄']['xpath']).click()
    sleep(3)
    driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
    sleep(5)


def clean_game_video(driver, elementinfo, cleanway='删除'):
    driver.find_element_by_xpath(elementinfo['比赛视频']['xpath']).click()
    sleep(2)
    driver.find_element_by_xpath("//android.widget.TextView[@text='选择']").click()
    sleep(1)
    driver.find_element_by_xpath(elementinfo['比赛视频']['xpath']).click()
    sleep(2)
    driver.find_element_by_xpath(f"//android.widget.TextView[@text='{cleanway}']").click()
    sleep(1)
    driver.find_element_by_id("android:id/button1").click()
    sleep(1)
    driver.back()
    sleep(2)


def joingame(driver_A, driver_B, devicename):
    failcount = 10  # 用例中出错后重新执行的次数
    runcount = 1
    num = 1
    elementinfo, deviceid = pubfuc.getiteminfo(driver_A.desired_capabilities, "zuji")
    while True:
        try:
            if runcount > failcount:
                break
            while num < 501:
                logger.info(f'第{num}次开始比赛')
                create_game(driver_A, elementinfo)
                game_code = get_game_code(driver_A, elementinfo)
                join_game_by_code(driver_B, elementinfo, game_code)

                driver_A.find_element_by_xpath(elementinfo['开始比赛']['xpath']).click()
                sleep(2)
                driver_A.find_element_by_id("android:id/button1").click()
                sleep(10)

                # 结束比赛
                driver_A.find_element_by_xpath(elementinfo['结束比赛']['xpath']).click()
                sleep(2)
                driver_A.find_element_by_id("android:id/button1").click()
                sleep(1)
                driver_A.find_element_by_id("android:id/button1").click()
                driver_B.find_element_by_id("android:id/button1").click()
                sleep(8)

                # 清理视频
                clean_game_video(driver_A, elementinfo)
                clean_game_video(driver_B, elementinfo)

                num += 1
            break
        except Exception as e:
            logger.info(f'第{num}次运行出错')
            err_time = pubfuc.getlocaltime()
            img_file = pubfuc.get_real_dir_path(__file__, f'../testresult/{err_time}-{devicename}.png')
            driver_A.save_screenshot(str(img_file))
            img_file = pubfuc.get_real_dir_path(__file__, f'../testresult/{err_time}-{devicename}-B.png')
            driver_B.save_screenshot(str(img_file))
            sleep(3)
            logger.error(e.args[0], exc_info=True)
            logger.info(f'第{runcount}次重跑')
            runcount += 1
            driver_A.close_app()
            driver_A.launch_app()
            driver_B.close_app()
            driver_B.launch_app()
            logger.info(pubfuc.getlocaltime())
            sleep(20)


def playgamevideo(driver, devicename):
    failcount = 3  # 用例中出错后重新执行的次数
    runcount = 1
    num = 1
    elementinfo, deviceid = pubfuc.getiteminfo(driver.desired_capabilities, "zuji")

    while True:
        try:
            if runcount > failcount:
                break
            driver.find_element_by_xpath("//android.widget.TextView[@text='lidw的主队']").click()
            sleep(2)
            driver.find_element_by_xpath(elementinfo['视频']['xpath']).click()
            sleep(3)
            phone_size = driver.get_window_size()
            size = driver.find_element_by_xpath(elementinfo['视频播放器']['xpath']).size
            print(phone_size, size)
            while num < 501:
                logger.info(f'第{num}次播放视频')
                driver.tap([[300, 400]])
                driver.swipe(start_x=size['width'] * 0.2, start_y=size['height'] * 0.7, end_x=size['width'] * 0.5,
                             end_y=size['height'] * 0.7,duration=3000)
                sleep(10)
                driver.tap([[300, 400]])
                driver.swipe(start_x=size['width'] * 0.2, start_y=size['height'] * 0.7, end_x=size['width'] * 0.5,
                             end_y=size['height'] * 0.7, duration=3000)
                sleep(10)
                driver.tap([[300, 400]])
                driver.swipe(start_x=size['width'] * 0.2, start_y=size['height'] * 0.7, end_x=size['width'] * 0.5,
                             end_y=size['height'] * 0.7, duration=3000)
                sleep(10)

                driver.tap([[300, 400]])
                sleep(0.5)
                driver.find_element_by_xpath(elementinfo['视频全屏']['xpath']).click()

                sleep(10)
                driver.tap([[300, 400]])
                sleep(0.5)
                driver.find_element_by_xpath(elementinfo['视频切换多视频']['xpath']).click()
                sleep(2)
                driver.back()
                num += 1
            break
        except Exception as e:
            logger.info(f'第{num}次运行出错')
            err_time = pubfuc.getlocaltime()
            img_file = pubfuc.get_real_dir_path(__file__, f'../testresult/{err_time}-{devicename}.png')
            driver.save_screenshot(str(img_file))
            sleep(3)
            logger.error(e.args[0], exc_info=True)
            logger.info(f'第{runcount}次重跑')
            runcount += 1
            driver.close_app()
            driver.launch_app()
            logger.info(pubfuc.getlocaltime())
            sleep(20)
