# -*- coding:utf-8 -*-
import sys,re,subprocess,traceback
# sys.path.append('..')

from time import sleep
import unittest
import lib.public_functions as pubfuc
from pathlib import Path
import multiprocessing,logging
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import testcase.app_behavior as app_behavior

class iRoomTest(unittest.TestCase):

    def setUp(self):
        self.控件信息 = pubfuc.获取控件文件信息()['iRoom_Android']
        #第一个为主播
        devicelist = ['ip8','ip7']
        # devicelist = ['p10_295']
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
            proc = pool.apply_async(app_behavior.加入离开房间, (driver, '5587',))
            procs.append(proc)
        for i in procs:
            i.get()
        for i in procs:
            i.wait()


    def test_002参与者多次切换角色(self):
        procs = []
        pool = multiprocessing.Pool(processes=len(self.driverlist))
        for driver in self.driverlist:
            proc = pool.apply_async(app_behavior.切换角色, (driver, '5602',))
            procs.append(proc)
        for i in procs:
            i.get()
        for i in procs:
            i.wait()


    def test_003参与者多次切后台(self):
        procs = []
        pool = multiprocessing.Pool(processes=len(self.driverlist))
        for driver in self.driverlist:
            proc = pool.apply_async(app_behavior.切后台, (driver, '5167',))
            procs.append(proc)
        for i in procs:
            i.get()
        for i in procs:
            i.wait()


    def test_004参与者多次加入离开指导房间(self):
        procs = []
        pool = multiprocessing.Pool(processes=len(self.driverlist))
        for driver in self.driverlist:
            proc = pool.apply_async(app_behavior.创建房间, (driver,))
            procs.append(proc)
        for i in procs:
            i.get()
        for i in procs:
            i.wait()

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
        # pass
        for driver in self.driverlist:
            driver.quit()
        for proc in self.proc_list:
            # print(proc.is_alive())
            proc.terminate()
            # proc.kill()
        #clean the node process,appium server is started by node
        # pubfuc.cleanNodeProcess()





