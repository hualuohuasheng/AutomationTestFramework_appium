# -*- coding:utf-8 -*-

from time import sleep
import lib.public_functions as pubfuc
from pathlib import Path
import traceback,re
from appium.webdriver.common.touch_action import TouchAction


def 选择大厅列表(driver,控件信息,大厅类型= '多人群聊'):
    大厅控件 = 控件信息['多人群聊']['xpath']
    if 大厅类型 != '多人群聊':
        大厅控件 = re.sub('多人群聊',大厅类型,大厅控件)
    driver.find_element_by_xpath(大厅控件).click()
    sleep(5)
    isIOS = 'desired' not in driver.desired_capabilities
    roompartern = 'RoomId' if isIOS else 'RoomID'
    success_flag = roompartern not in driver.page_source
    while success_flag:
        sleep(3)
        success_flag = roompartern not in driver.page_source



def 选择房间加入(driver,控件信息,roomxpath):
    roomisfind = re.findall('Room\w+',roomxpath)[0] in driver.page_source
    if roomisfind:
        driver.find_element_by_xpath(roomxpath).click()
    else:
        print(driver.page_source)
        driver.find_element_by_xpath(roomxpath).click()
    sleep(5)
    if not driver.find_element_by_id(控件信息['JOIN']['id']).get_attribute('enabled'):
        driver.back()
        sleep(1)
        driver.find_element_by_xpath(roomxpath).click()
        sleep(3)
    driver.find_element_by_id(控件信息['JOIN']['id']).click()
    sleep(5)
    是否加入成功 = 控件信息['离开房间']['id'] in driver.page_source
    print(f'加入房间成功:{是否加入成功}')

def 加入离开房间(driver,roomid):
    failcount = 0# 用例中出错后重新执行的次数
    runcount = 1
    success_flag = True
    num = 1
    while success_flag:
        try:
            if runcount > failcount:
                success_flag = False
            devicedriverinfo = driver.desired_capabilities  # 获取正在运行的设备的参数设置
            print(devicedriverinfo)
            isIOS = 'desired' not in devicedriverinfo
            控件信息, deviceid = pubfuc.获取控件信息(devicedriverinfo)
            roomid = f' {roomid}' if isIOS else roomid
            while num < 201:
                if num == 1:
                    选择大厅列表(driver,控件信息)
                roomxpath = re.sub("xxxx", roomid, 控件信息['房间列表']['xpath'])
                print(f"第{num}次{deviceid}加入房间")
                选择房间加入(driver, 控件信息, roomxpath)
                # pubfuc.waittimeout(driver.find_element_by_id(控件信息['JOIN']['id']))
                sleep(10)
                driver.find_element_by_id(控件信息['离开房间']['id']).click()
                sleep(6)
                num += 1
        except Exception as e:
            loctime = pubfuc.getLocalTime()
            print(deviceid,loctime)
            print(driver.page_source)
            img_file = Path(__file__).cwd().parent / 'testresult' / f'{loctime}-{deviceid}.png'
            driver.save_screenshot(str(img_file))
            sleep(3)
            print(e.args[0])
            traceback.print_exc()
            if not success_flag:
                return
            runcount += 1
            driver.close_app()
            driver.launch_app()
            num = 1


def 切换角色(driver,roomid):
    failcount = 1  # 用例中出错后重新执行的次数
    runcount = 1
    success_flag = True
    num = 1
    while success_flag:
        try:
            if runcount > failcount:
                success_flag = False
            devicedriverinfo = driver.desired_capabilities  # 获取正在运行的设备的参数设置
            print(devicedriverinfo)
            isIOS = 'desired' not in devicedriverinfo
            控件信息, deviceid = pubfuc.获取控件信息(devicedriverinfo)
            # 选择多人群聊
            选择大厅列表(driver, 控件信息)
            sleep(5)
            roomid = f' {roomid}' if isIOS else roomid
            roomxpath = re.sub("xxxx", roomid, 控件信息['房间列表']['xpath'])
            # 加入房间
            选择房间加入(driver, 控件信息, roomxpath)
            sleep(10)
            if 控件信息['离开房间']['id'] not in driver.page_source:
                raise RuntimeError('加入房间失败')
            while num < 201:
                print(f"第{num}次{deviceid}切换角色")
                print(driver.find_element_by_id(控件信息['切换角色']['id']).get_attribute('enabled'))
                driver.find_element_by_id(控件信息['切换角色']['id']).click()
                sleep(20)
                num += 1
        except Exception as e:
            loctime = pubfuc.getLocalTime()
            print(deviceid, loctime)
            print(driver.page_source)
            img_file = Path(__file__).cwd().parent / 'testresult' / f'{loctime}-{deviceid}.png'
            driver.save_screenshot(str(img_file))
            sleep(3)
            print(e.args[0])
            traceback.print_exc()
            if not success_flag:
                return
            print(f'第{runcount}次重跑')
            runcount += 1
            driver.close_app()
            driver.launch_app()
            num = 1


def 切后台(driver,roomid):
    try:
        devicedriverinfo = driver.desired_capabilities  # 获取正在运行的设备的参数设置
        print(devicedriverinfo)
        isIOS = 'desired' not in devicedriverinfo
        控件信息, deviceid = pubfuc.获取控件信息(devicedriverinfo)
        # click 多人群聊
        driver.find_element_by_xpath(控件信息['多人群聊']['xpath']).click()
        sleep(3)
        roomid = f' {roomid}' if isIOS else roomid
        roomxpath = re.sub("xxxx", roomid, 控件信息['房间列表']['xpath'])
        pubfuc.waittimeout(driver.find_element_by_xpath(roomxpath))
        # click 房间
        driver.find_element_by_xpath(roomxpath).click()
        # pubfuc.waittimeout(driver.find_element_by_id(控件信息['JOIN']['id']))
        sleep(5)
        if not driver.find_element_by_id(控件信息['JOIN']['id']).get_attribute('enabled'):
            sleep(3)
        driver.find_element_by_id(控件信息['JOIN']['id']).click()
        sleep(10)
        num = 1
        while num < 501:
            print(f"第{num}次{deviceid}切后台")
            driver.background_app(5)
            sleep(5)
            # 切后台回来后，查看离开房间按钮是否可用，确定正确切回了前台
            print(driver.find_element_by_id(控件信息['离开房间']['id']).get_attribute('enabled'))
            num += 1
    except Exception as e:
        loctime = pubfuc.getLocalTime()
        print(deviceid, loctime)
        print(driver.page_source)
        img_file = Path(__file__).cwd().parent / 'testresult' / f'{loctime}-{deviceid}.png'
        driver.save_screenshot(str(img_file))
        sleep(3)
        print(e.args[0])
        traceback.print_exc()


def 创建房间(driver):
    try:
        devicedriverinfo = driver.desired_capabilities  # 获取正在运行的设备的参数设置
        print(devicedriverinfo)
        控件信息, deviceid = pubfuc.获取控件信息(devicedriverinfo)
        选择大厅列表(driver,控件信息)
        num = 1
        while num <101:
            print(f'{num}次创建房间')
            driver.find_element_by_id(控件信息['创建房间']['id']).click()
            sleep(2)
            driver.find_element_by_xpath(控件信息['START']['xpath']).click()
            sleep(3)
            driver.find_element_by_id(控件信息['RoomID']['id']).click()
            sleep(2)
            print(driver.find_element_by_id(控件信息['推流信息']['id']).get_attribute('text'))
            sleep(5)

            driver.find_element_by_id(控件信息['离开房间']['id']).click()
            sleep(4)
            num += 1
        # 选择房间加入(driver,控件信息,roomxpath)
    except Exception as e:
        loctime = pubfuc.getLocalTime()
        print(deviceid, loctime)
        print(driver.page_source)
        img_file = Path(__file__).cwd().parent / 'testresult' / f'{loctime}-{deviceid}.png'
        driver.save_screenshot(str(img_file))
        sleep(3)
        print(e.args[0])
        traceback.print_exc()