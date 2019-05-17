# -*- coding:utf-8 -*-

from time import sleep
import lib.public_functions as pubfuc
from pathlib import Path
import re
import subprocess
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


def start_match(driver, devicename):
    # 260, 320, 380
    # 再来一局
    # //XCUIElementTypeButton[@name="再来一局"]
    failcount = 3  # 用例中出错后重新执行的次数
    runcount = 1
    num = 1
    devicedriverinfo = driver.desired_capabilities  # 获取正在运行的设备的参数设置
    elementinfo, deviceid = pubfuc.getiteminfo(devicedriverinfo, 'zhifou')
    while True:
        try:
            if runcount > failcount:
                break
            driver.find_element_by_id(elementinfo['开始比赛']['id']).click()
            sleep(3)
            driver.find_element_by_xpath(elementinfo['开始匹配_好好学习']['xpath']).click()
            sleep(25)
            if elementinfo['退出房间']['id'] not in driver.page_source:
                raise RuntimeError('加入房间失败')

            size = driver.get_window_size()

            for i in range(100):
                driver.tap([[size['width'] / 2, 260]])
                sleep(2)

            sleep(2)
            driver.find_element_by_id(elementinfo['退出房间']['id']).click()
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