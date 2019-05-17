# -*- coding:utf-8 -*-
import re
from time import sleep
import unittest
import lib.public_functions as pubfuc
import multiprocessing
from appium import webdriver
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