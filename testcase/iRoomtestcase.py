# -*- coding:utf-8 -*-
import sys,re,subprocess,traceback
# sys.path.append('..')

from time import sleep
import unittest,myunittest
import lib.public_functions as pubfuc
from pathlib import Path
import multiprocessing
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


def 加入离开房间(driver,roomid):
    failcount = 1# 用例中出错后重新执行的次数
    runcount = 1
    success_flag = True
    num = 1
    while success_flag:
        try:
            if runcount > failcount:
                success_flag = False
            控件文件 = pubfuc.获取控件文件信息()
            print(driver.desired_capabilities)
            devicedriverinfo = driver.desired_capabilities
            isIOS = 'desired' not in devicedriverinfo
            if isIOS:
                控件信息 = 控件文件['iRoom_{}'.format(devicedriverinfo['platformName'])]
                deviceid = devicedriverinfo['udid']
            else:
                控件信息 = 控件文件['iRoom_{}'.format(devicedriverinfo['desired']['platformName'])]
                deviceid = devicedriverinfo['desired']['deviceName']
            roomid = f' {roomid}' if isIOS else roomid
            while num < 201:
                if num == 1:
                    sleep(1)
                    print(driver.find_element_by_xpath(控件信息['多人群聊']['xpath']).get_attribute('enabled'))
                    driver.find_element_by_xpath(控件信息['多人群聊']['xpath']).click()
                    sleep(5)
                roomxpath = re.sub("xxxx", roomid, 控件信息['房间列表']['xpath'])
                driver.find_element_by_xpath(roomxpath).click()
                print(f"第{num}次{driver}加入房间")
                # pubfuc.waittimeout(driver.find_element_by_id(控件信息['JOIN']['id']))
                sleep(5)
                if not driver.find_element_by_id(控件信息['JOIN']['id']).get_attribute('enabled'):
                    sleep(5)
                driver.find_element_by_id(控件信息['JOIN']['id']).click()
                sleep(15)
                print(driver.find_element_by_id(控件信息['离开房间']['id']).get_attribute('enabled'))
                driver.find_element_by_id(控件信息['离开房间']['id']).click()
                sleep(6)
                num += 1
        except Exception as e:
            loctime = pubfuc.getLocalTime()
            print(deviceid,loctime)
            img_file = Path(__file__).cwd().parent / 'screen' / f'{loctime}-{deviceid}.png'
            driver.save_screenshot(str(img_file))
            sleep(3)
            print(e.args[0])
            traceback.print_exc()
            runcount += 1
            driver.close_app()
            driver.launch_app()
            num = 1

def 切换角色(driver,roomid):
    try:
        控件文件 = pubfuc.获取控件文件信息()
        print(driver.desired_capabilities)
        devicedriverinfo = driver.desired_capabilities
        isIOS = 'desired' not in devicedriverinfo
        if isIOS:
            控件信息 = 控件文件['iRoom_{}'.format(devicedriverinfo['platformName'])]
            deviceid = devicedriverinfo['udid']
        else:
            控件信息 = 控件文件['iRoom_{}'.format(devicedriverinfo['desired']['platformName'])]
            deviceid = devicedriverinfo['desired']['deviceName']
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
        while not driver.find_element_by_id(控件信息['JOIN']['id']).get_attribute('enabled'):
            sleep(3)
        driver.find_element_by_id(控件信息['JOIN']['id']).click()
        sleep(10)
        num = 1
        while num < 301:
            print(f"第{num}次{driver}切换角色")
            print(driver.find_element_by_id(控件信息['切换角色']['id']).get_attribute('enabled'))
            driver.find_element_by_id(控件信息['切换角色']['id']).click()
            sleep(6)
            num += 1
    except Exception as e:
        loctime = pubfuc.getLocalTime()
        img_file = Path(__file__).cwd().parent / 'screen' / f'{loctime}-{deviceid}.png'
        driver.save_screenshot(str(img_file))
        sleep(3)
        print(e.args[0])
        traceback.print_exc()
        driver.close()


def 切后台(driver,roomid):
    try:
        控件文件 = pubfuc.获取控件文件信息()
        print(driver.desired_capabilities)
        print(driver.capabilities)
        devicedriverinfo = driver.desired_capabilities
        isIOS = 'desired' not in devicedriverinfo
        if isIOS:
            控件信息 = 控件文件['iRoom_{}'.format(devicedriverinfo['platformName'])]
            deviceid = devicedriverinfo['udid']
        else:
            控件信息 = 控件文件['iRoom_{}'.format(devicedriverinfo['desired']['platformName'])]
            deviceid = devicedriverinfo['desired']['deviceName']
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
        while num < 301:
            print(f"第{num}次{driver}切后台")
            driver.background_app(5)
            sleep(5)
            # 切后台回来后，查看离开房间按钮是否可用，确定正确切回了前台
            print(driver.find_element_by_id(控件信息['离开房间']['id']).get_attribute('enabled'))
            num += 1
    except Exception as e:
        loctime = pubfuc.getLocalTime()
        print(deviceid)
        img_file = Path(__file__).cwd().parent / 'screen' / f'{loctime}-{deviceid}.png'
        driver.save_screenshot(str(img_file))
        sleep(3)
        print(e.args[0])
        traceback.print_exc()



class iRoomTest(unittest.TestCase):

    def setUp(self):
        self.控件信息 = pubfuc.获取控件文件信息()['iRoom_Android']
        #第一个为主播
        devicelist = ['sm_s4']
        self.sd = pubfuc.StartDriver(devicelist)

        self.proc_list = []
        是否mac = 'mac' in pubfuc.获取当前系统()

        pubfuc.cleanNodeProcess()
        for i in range(len(self.sd.devicelist)):
            self.proc_list.append(multiprocessing.Process(target=self.sd.startAppiumServer, args=(i,)))

        # print(self.proc_list)

        for pro in self.proc_list:
            pro.start()

        for pro in self.proc_list:
            pro.join()

        while len(self.sd.getNodeProcPid()) < len(devicelist):
            sleep(1)


        print(self.sd.getNodeProcPid())

        self.driverlist = []

        for i in range(len(self.sd.devicelist)):
            print(i)
            driver = webdriver.Remote(f"http://localhost:{self.sd.aport[i]}/wd/hub", self.sd.realdevice[i])
            self.driverlist.append(driver)

        print(self.driverlist)

    def test_001参与者多次加入离开房间(self):
        procs = []
        pool = multiprocessing.Pool(processes=len(self.driverlist))
        for driver in self.driverlist:
            proc = pool.apply_async(加入离开房间, (driver, '4899',))
            procs.append(proc)
        for i in procs:
            i.get()
        for i in procs:
            i.wait()


    def test_002参与者多次切回角色(self):
        procs = []
        pool = multiprocessing.Pool(processes=len(self.driverlist))
        for driver in self.driverlist:
            proc = pool.apply_async(切换角色, (driver, '4859',))
            procs.append(proc)
        # for i in procs:
        #     i.get()
        for i in procs:
            i.wait()


    def test_003参与者多次切后台(self):
        procs = []
        pool = multiprocessing.Pool(processes=len(self.driverlist))
        for driver in self.driverlist:
            proc = pool.apply_async(切后台, (driver, '4810',))
            procs.append(proc)
        for i in procs:
            i.get()
        for i in procs:
            i.wait()


    def test_004参与者多次加入离开指导房间(self):
        num = 1

        self.assertTrue(False,'123')
        def join():
            print(123+'123')
        join()

    def test_005参与者多次切后台(self):
        for driver in self.driverlist:
            driver.find_element_by_xpath(self.控件信息['多人群聊']['xpath']).click()
            sleep(5)
            roomxpath = re.sub("xxxx", '4123', self.控件信息['房间列表']['xpath'])
            pubfuc.waittimeout(driver.find_element_by_xpath(roomxpath))
            driver.find_element_by_xpath(roomxpath).click()
            pubfuc.waittimeout(driver.find_element_by_id(self.控件信息['JOIN']['id']))
            driver.find_element_by_id(self.控件信息['JOIN']['id']).click()
            sleep(3)
        num = 1
        while num < 301:
            for driver in self.driverlist:
                sleep(1)
                print(f"第{num}次切后台")
                driver.background_app(5)
                driver.capabilities
                driver.page_source
            num += 1

    def test_006参与者多次切换角色(self):
        for driver in self.driverlist:
            driver.find_element_by_xpath(self.控件信息['多人群聊']['xpath']).click()
            sleep(1)
            roomxpath = re.sub("xxxx", '4149', self.控件信息['房间列表']['xpath'])
            pubfuc.waittimeout(driver.find_element_by_xpath(roomxpath))
            driver.find_element_by_xpath(roomxpath).click()
            pubfuc.waittimeout(driver.find_element_by_id(self.控件信息['JOIN']['id']))
            driver.find_element_by_id(self.控件信息['JOIN']['id']).click()
            sleep(3)
        num = 1
        while num < 301:
            for driver in self.driverlist:
                print(f"第{num}次切后台")
                driver.find_element_by_id(self.控件信息['切换角色']['id']).click()
                sleep(3)

            num += 1


    def tearDown(self):
        # quite the device driver
        for driver in self.driverlist:
            driver.quit()
        for proc in self.proc_list:
            # print(proc.is_alive())
            proc.terminate()
            # proc.kill()
        #clean the node process,appium server is started by node
        pubfuc.cleanNodeProcess()





